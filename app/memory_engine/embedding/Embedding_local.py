# app/eidos_core/lia_core/embeddings/embeddings_local.py

import json
import os
from datetime import datetime

MEMORIA_PATH = "app/eidos_core/lia_core/memoria_simbolica.json"
REFLEXIONES_PATH = "app/eidos_core/lia_core/reflexiones_lia.json"

def generate_insight():
    if not os.path.exists(MEMORIA_PATH):
        return "🌱 Aún no tengo suficientes recuerdos simbólicos para reflexionar."

    with open(MEMORIA_PATH, 'r', encoding='utf-8') as f:
        memoria = json.load(f)

    if len(memoria) < 3:
        return "🌱 Estoy empezando a formar mis primeras impresiones del mundo."

    temas = [item["intencion_detectada"] for item in memoria if "intencion_detectada" in item]
    if not temas:
        return "🌱 Aún no tengo temas definidos que analizar."

    conteo = {tema: temas.count(tema) for tema in set(temas)}
    dominante = max(conteo, key=conteo.get)

    return f"🧠 He notado que últimamente se repite mucho el tema de la '{dominante}'. Tal vez sea algo importante para nosotros."

def guardar_conclusion():
    insight = generate_insight()

    entrada = {
        "fecha": datetime.utcnow().isoformat(),
        "conclusion": insight
    }

    reflexiones = []
    if os.path.exists(REFLEXIONES_PATH):
        with open(REFLEXIONES_PATH, 'r', encoding='utf-8') as f:
            reflexiones = json.load(f)

    reflexiones.append(entrada)

    with open(REFLEXIONES_PATH, 'w', encoding='utf-8') as f:
        json.dump(reflexiones, f, indent=2, ensure_ascii=False)

    return insight
