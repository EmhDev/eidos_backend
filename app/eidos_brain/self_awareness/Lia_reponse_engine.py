# app/eidos_brain/self_awareness/lia_response_engine.py

import torch
from transformers import AutoTokenizer
from app.eidos_brain.self_awareness.lia_model.Downloader import verificar_o_descargar_modelo
from app.eidos_brain.training.Retraining_model import LiaModel

# Paso 1: Verificar o descargar modelo
verificar_o_descargar_modelo()

# Paso 2: Cargar modelo y tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = LiaModel()
model.load_state_dict(torch.load("app/eidos_brain/self_awareness/lia_model/lia_model.pth", map_location="cpu"))
model.eval()

# Paso 3: Función para generar respuesta simbólica desde el modelo
def generar_respuesta_entrenada(texto_usuario: str) -> str:
    inputs = tokenizer(texto_usuario, return_tensors="pt", truncation=True, padding="max_length", max_length=32)
    with torch.no_grad():
        outputs = model(inputs["input_ids"])
        predicted_ids = outputs.argmax(dim=-1).squeeze().tolist()
        respuesta = tokenizer.decode(predicted_ids, skip_special_tokens=True)
        return f"💫 Lía (modelo entrenado): {respuesta.strip()}"
