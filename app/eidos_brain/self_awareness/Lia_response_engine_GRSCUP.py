# app/eidos_brain/self_awareness/lia_response_engine_GRSCUP.py

import torch
from transformers import AutoTokenizer, AutoModel
from pathlib import Path
import torch.nn as nn
import os
from app.eidos_brain.self_awareness.lia_model.Downloader import verificar_o_descargar_modelo
from app.eidos_brain.training.Retraining_model import LiaModel

# 📜 Configuración del modelo
MODEL_PATH = os.getenv("MODEL_PATH", "app/eidos_brain/self_awareness/lia_model/lia_model_GRSCUP_v1.pth")

# Inicialización de tokenizer y modelo base BERT
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# 💤 Lazy Loading del modelo entrenado
model = None

def generar_respuesta_lia(texto_usuario: str) -> str:
    global model
    if model is None:
        print("📥 Cargando modelo neuronal de Lía por primera vez...")
        verificar_o_descargar_modelo()
        model = LiaModel()  # reconstruimos arquitectura
        model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
        model.eval()
        print("✅ Modelo cargado correctamente.")

    entrada = tokenizer(texto_usuario, padding="max_length", truncation=True, max_length=32, return_tensors="pt")
    with torch.no_grad():
        output = model(entrada["input_ids"], entrada["attention_mask"])
        predicted_ids = torch.argmax(output, dim=2)
        respuesta = tokenizer.decode(predicted_ids[0], skip_special_tokens=True)
    return respuesta.strip()
