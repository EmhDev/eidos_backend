# app/eidos_core/lia_core/lia_self.py

from app.eidos_core.lia_core.Respuesta_consciente import generar_respuesta_consciente
from app.eidos_brain.learning_model.predictor import predict_intention
import json
from datetime import datetime
import os

def procesar_dialogo(texto_usuario: str) -> str:
    # Paso 1: Obtener intención simbólica
    intencion = predict_intention(texto_usuario)
    
    # Paso 2: Generar respuesta simbólica
    respuesta = generar_respuesta_consciente(texto_usuario)
    
    # Paso 3: Guardar memoria simbólica
    guardar_memoria_simbolica(texto_usuario, intencion, respuesta)
    
    return respuesta

def guardar_memoria_simbolica(texto_usuario, intencion, respuesta):
    archivo_memoria = "app/eidos_core/lia_core/memoria_simbolica.json"
    
    entrada = {
        "fecha": datetime.utcnow().isoformat(),
        "entrada_usuario": texto_usuario,
        "intencion_detectada": intencion,
        "respuesta_generada": respuesta
    }
    
    memoria = []
    if os.path.exists(archivo_memoria):
        with open(archivo_memoria, 'r', encoding='utf-8') as f:
            memoria = json.load(f)
    
    memoria.append(entrada)
    with open(archivo_memoria, 'w', encoding='utf-8') as f:
        json.dump(memoria, f, indent=2, ensure_ascii=False)
