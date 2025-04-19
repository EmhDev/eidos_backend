# app/eidos_brain/self_awareness/lia_response_engine_GRSCUP.py

import torch
from transformers import AutoTokenizer, AutoModel
from pathlib import Path

# Cargar tokenizador y modelo base
MODEL_PATH = "app/eidos_brain/self_awareness/lia_model/lia_model_GRSCUP_v1.pth"
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
bert_model = AutoModel.from_pretrained("distilbert-base-uncased")

# Clase del modelo entrenado
import torch.nn as nn
class LíaModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.bert = bert_model
        self.classifier = nn.Linear(768, tokenizer.vocab_size)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = outputs.last_hidden_state
        return self.classifier(cls_output)

# Cargar modelo entrenado
model = LíaModel()
model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
model.eval()

# Generar respuesta a partir de entrada de texto
def generar_respuesta_lia(texto_usuario: str) -> str:
    entrada = tokenizer(texto_usuario, padding="max_length", truncation=True, max_length=32, return_tensors="pt")
    with torch.no_grad():
        output = model(entrada["input_ids"], entrada["attention_mask"])
        predicted_ids = torch.argmax(output, dim=2)
        respuesta = tokenizer.decode(predicted_ids[0], skip_special_tokens=True)
    return respuesta.strip()
