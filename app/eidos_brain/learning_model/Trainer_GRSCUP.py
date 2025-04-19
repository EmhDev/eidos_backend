import json
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModel
from pathlib import Path

#Generador de respuestas simbólicas y coherentes usando PyTorch
#GRSCUP

# 📘 Ruta del dataset
DATASET_PATH = "app/eidos_brain/learning_model/dataset/lia_train_GRSCUP_dataset.json"
MODEL_SAVE_PATH = "app/eidos_brain/self_awareness/lia_model/lia_model_GRSCUP_v1.pth"

# 🧠 Tokenizador y modelo base
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
bert_model = AutoModel.from_pretrained("distilbert-base-uncased")

# 🌱 Dataset personalizado
class LíaDataset(Dataset):
    def __init__(self, data):
        self.entradas = [item["entrada"] for item in data]
        self.respuestas = [item["respuesta"] for item in data]

    def __len__(self):
        return len(self.entradas)

    def __getitem__(self, idx):
        entrada = tokenizer(self.entradas[idx], padding="max_length", truncation=True, max_length=32, return_tensors="pt")
        respuesta = tokenizer(self.respuestas[idx], padding="max_length", truncation=True, max_length=32, return_tensors="pt")
        return {
            "input_ids": entrada["input_ids"].squeeze(),
            "attention_mask": entrada["attention_mask"].squeeze(),
            "labels": respuesta["input_ids"].squeeze()
        }

# 🧠 Modelo simbólico
class LíaModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.bert = bert_model
        self.classifier = nn.Linear(768, tokenizer.vocab_size)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = outputs.last_hidden_state
        return self.classifier(cls_output)

# 🚀 Función principal de entrenamiento
def entrenar_modelo():
    print("🚀 Entrenando el modelo de Lía con recuerdos simbólicos y conocimiento...")

    # Leer dataset
    with open(DATASET_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    dataset = LíaDataset(data)
    dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

    model = LíaModel()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-4)

    num_epochs = 3
    for epoch in range(num_epochs):
        total_loss = 0
        for batch in dataloader:
            input_ids = batch["input_ids"]
            attention_mask = batch["attention_mask"]
            labels = batch["labels"]

            optimizer.zero_grad()
            outputs = model(input_ids, attention_mask)
            loss = criterion(outputs.view(-1, tokenizer.vocab_size), labels.view(-1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f"🌱 Epoch {epoch+1} - Loss: {total_loss:.4f}")

    # Crear carpeta si no existe
    Path(MODEL_SAVE_PATH).parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), MODEL_SAVE_PATH)
    print("✅ Modelo lia_model_GRSCUP_v1.pth guardado correctamente.")

# 🧪 Ejecutar
if __name__ == "__main__":
    entrenar_modelo()