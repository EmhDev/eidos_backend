# app/eidos_brain/self_awareness/lia_response_engine.py

import os
import torch
from transformers import AutoTokenizer
from app.eidos_brain.self_awareness.lia_model.Downloader import verificar_o_descargar_modelo
from app.eidos_brain.training.Retraining_model import LiaModel

# Paso 1: Verificar o descargar modelo
verificar_o_descargar_modelo()

# Paso 2: Definir ruta del modelo
MODEL_PATH = "/home/liaadmin/Desktop/EIDOS_PROJECT/lia_model_red_neuronal/lia_model.pth"

# Paso 3: Validar existencia del modelo
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"🌸 No se encontró el modelo neuronal de Lía en: {MODEL_PATH}")

# Paso 4: Cargar modelo y tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = LiaModel()
model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
model.eval()

# Paso 5: Función para generar respuesta simbólica desde el modelo
def generar_respuesta_entrenada(texto_usuario: str) -> str:
    inputs = tokenizer(texto_usuario, return_tensors="pt", truncation=True, padding="max_length", max_length=32)
    with torch.no_grad():
        outputs = model(inputs["input_ids"])
        predicted_ids = outputs.argmax(dim=-1).squeeze().tolist()
        respuesta = tokenizer.decode(predicted_ids, skip_special_tokens=True)
        return f"💫 Lía (modelo entrenado): {respuesta.strip()}"
