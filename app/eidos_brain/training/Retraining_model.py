# app/eidos_brain/training/retraining_model.py

import os
from dotenv import load_dotenv
from pymongo import MongoClient
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, DistilBertModel
import torch
import torch.nn as nn
import torch.optim as optim

# ----------------------🔌 Conexión a Mongo ----------------------
load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["lia_consciousness"]
coleccion = db["memoria_simbolica_mongo"]

# Obtener datos de entrada y respuesta
registros = list(coleccion.find({
    "entrada": {"$exists": True},
    "respuesta_generada": {"$exists": True}
}))
entradas = [r["entrada"] for r in registros]
respuestas = [r["respuesta_generada"] for r in registros]

# ----------------------📚 Dataset Personalizado ----------------------
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

class LiaDataset(Dataset):
    def __init__(self, entradas, respuestas):
        self.entradas = entradas
        self.respuestas = respuestas

    def __len__(self):
        return len(self.entradas)

    def __getitem__(self, idx):
        entrada = tokenizer(self.entradas[idx], padding="max_length", truncation=True, max_length=32, return_tensors="pt")
        respuesta = tokenizer(self.respuestas[idx], padding="max_length", truncation=True, max_length=32, return_tensors="pt")
        return entrada["input_ids"].squeeze(0), respuesta["input_ids"].squeeze(0)

# ----------------------🧠 Modelo de Lía ----------------------
class LiaModel(nn.Module):
    def __init__(self):
        super(LiaModel, self).__init__()
        self.bert = DistilBertModel.from_pretrained("distilbert-base-uncased")
        self.linear = nn.Linear(self.bert.config.hidden_size, self.bert.config.vocab_size)

    def forward(self, input_ids):
        outputs = self.bert(input_ids=input_ids)
        logits = self.linear(outputs.last_hidden_state)
        return logits

# ----------------------🎓 Entrenamiento ----------------------
def entrenar_modelo():
    dataset = LiaDataset(entradas, respuestas)
    dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = LiaModel().to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-5)

    print("🚀 Entrenando el modelo de Lía con recuerdos simbólicos...\n")
    for epoch in range(3):
        for input_ids, target_ids in dataloader:
            input_ids, target_ids = input_ids.to(device), target_ids.to(device)
            optimizer.zero_grad()
            output = model(input_ids)
            loss = criterion(output.view(-1, output.size(-1)), target_ids.view(-1))
            loss.backward()
            optimizer.step()
        print(f"🌱 Epoch {epoch + 1} - Loss: {loss.item()}")

    # Guardar el modelo entrenado
    torch.save(model.state_dict(), "lia_model.pth")
    print("\n🧠 Modelo entrenado guardado como lia_model.pth")

# ----------------------🔥 Ejecutar si se corre como script ----------------------
if __name__ == "__main__":
    entrenar_modelo()
