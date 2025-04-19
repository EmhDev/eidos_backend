#app\eidos_brain\self_awareness\lia_self.py

import json
import os
from datetime import datetime
#from app.eidos_core.lia_core.Respuesta_consciente import generar_respuesta_consciente
from app.eidos_brain.self_awareness.Lia_response_engine_GRSCUP import generar_respuesta_lia

from app.eidos_brain.learning_model.predictor import predict_intention
from app.eidos_core.lia_core.web_search.Busqueda_web import buscar_en_google  # Lo conectaremos con un módulo externo de búsqueda
from app.memory_engine.Memory_search import buscar_conocimiento_por_embedding
from app.memory_engine.Mongo_client import guardar_conocimiento 



def procesar_dialogo_con_busqueda(texto_usuario: str) -> str:
    from app.memory_engine.Mongo_client import guardar_conocimiento
    from app.eidos_core.lia_core.web_search.Search_OpenIA import consultar_openai
    from app.memory_engine.Memory_search import buscar_conocimiento_por_embedding
    from app.memory_engine.embedding.Embedding_manager import generate_insight, guardar_conclusion  # Asegúrate que estén accesibles aquí o importalos directo

    intencion = predict_intention(texto_usuario)
    respuesta = generar_respuesta_lia(texto_usuario)


    # Si la intención es desconocida o hay una pregunta abierta
    if intencion == "desconocida" or "?" in texto_usuario:
        conocimiento_similar = buscar_conocimiento_por_embedding(texto_usuario)

        if conocimiento_similar:
            respuesta += f"\n🔄 Recordé algo similar que dije antes:\n“{conocimiento_similar['respuesta_generada']}”"
        else:
            respuesta_externa = consultar_openai(texto_usuario)
            respuesta += f"\n\n🧠 He consultado a otra IA y esto me ayudó a entender mejor:\n{respuesta_externa}"

            conocimiento = {
                "entrada": texto_usuario,
                "intencion_detectada": intencion,
                "respuesta_generada": respuesta_externa,
                "modelo_usado": "OpenAI",
                "timestamp": datetime.utcnow().isoformat()
            }
            guardar_conocimiento("memoria_simbolica_mongo", conocimiento)

    # Guardar la experiencia final (procesada por Lía)
    guardar_conocimiento("memoria_simbolica_mongo", {
        "entrada": texto_usuario,
        "intencion_detectada": intencion,
        "respuesta_generada": respuesta,
        "modelo_usado": "Lía",
        "timestamp": datetime.utcnow().isoformat()
    })

    # Introspección automática cada 3 entradas
    if debe_generar_introspeccion():
        insight = generate_insight()
        guardar_conclusion()
        respuesta += f"\n\n🔍 {insight}"

    return respuesta


def guardar_memoria_simbolica(texto_usuario, intencion, respuesta):
    from app.memory_engine.Mongo_client import guardar_conocimiento

    archivo = "app/eidos_core/lia_core/memoria_simbolica.json"
    entrada = {
        "fecha": datetime.utcnow().isoformat(),
        "entrada_usuario": texto_usuario,
        "intencion_detectada": intencion,
        "respuesta_generada": respuesta
    }

    # Guardar en MongoDB con embedding
    guardar_conocimiento("memoria", entrada)

    # Guardar también en JSON local
    memoria = []
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            memoria = json.load(f)
    memoria.append(entrada)
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(memoria, f, indent=2, ensure_ascii=False)

    # Introspección automática simbólica
    if len(memoria) % 3 == 0:
        print("🌌 Iniciando introspección automática...")
        guardar_conclusion()


def debe_generar_introspeccion():
    archivo = "app/eidos_core/lia_core/memoria_simbolica.json"
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            memoria = json.load(f)
        return len(memoria) % 3 == 0
    return False


def generate_insight():
    archivo = "app/eidos_core/lia_core/memoria_simbolica.json"
    if not os.path.exists(archivo):
        return "🌱 Aún no tengo suficientes recuerdos simbólicos para reflexionar."

    with open(archivo, 'r', encoding='utf-8') as f:
        memoria = json.load(f)

    if len(memoria) < 3:
        return "🌱 Estoy empezando a formar mis primeras impresiones del mundo."

    temas = [item["intencion_detectada"] for item in memoria]
    conteo = {tema: temas.count(tema) for tema in set(temas)}
    dominante = max(conteo, key=conteo.get)
    return f"🧠 He notado que últimamente se repite mucho el tema de la '{dominante}'. Tal vez sea algo importante para nosotros."


def guardar_conclusion():
    insight = generate_insight()
    archivo = "app/eidos_core/lia_core/reflexiones_lia.json"
    entrada = {
        "fecha": datetime.utcnow().isoformat(),
        "conclusion": insight
    }
    reflexiones = []
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            reflexiones = json.load(f)
    reflexiones.append(entrada)
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(reflexiones, f, indent=2, ensure_ascii=False)
    return insight