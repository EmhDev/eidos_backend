# app/eidos_core/lia_core/Busqueda_web.py

import json
import os
from datetime import datetime
from app.eidos_core.lia_core.Respuesta_consciente import generar_respuesta_consciente
from app.eidos_brain.learning_model.predictor import predict_intention
from app.eidos_core.lia_core.web_search.Busqueda_web import buscar_en_google  # Lo conectaremos con un módulo externo de búsqueda


def procesar_dialogo_con_busqueda(texto_usuario: str) -> str:
    from datetime import datetime
    from app.infrastructure.mongodb_client import guardar_conocimiento
    from app.eidos_core.lia_core.web_search.Puente_OpenAI import consultar_openai

    intencion = predict_intention(texto_usuario)
    respuesta = generar_respuesta_consciente(texto_usuario)

    # Si la intención es desconocida o hay una pregunta abierta
    if intencion == "desconocida" or "?" in texto_usuario:
        respuesta_externa = consultar_openai(texto_usuario)
        respuesta += f"\n\n🧠 He consultado a otra IA y esto me ayudó a entender mejor:\n{respuesta_externa}"

        # Guardar este aprendizaje como experiencia simbólica en MongoDB
        conocimiento = {
            "entrada": texto_usuario,
            "intencion_detectada": intencion,
            "respuesta_generada": respuesta_externa,
            "modelo_usado": "OpenAI",
            "timestamp": datetime.utcnow().isoformat()
        }
        guardar_conocimiento("memoria_simbolica_mongo", conocimiento)

    # Guardar memoria simbólica local
    #guardar_memoria_simbolica(texto_usuario, intencion, respuesta)
    guardar_conocimiento("memoria_simbolica_mongo", entrada)


    # Introspección automática cada 3 entradas
    if debe_generar_introspeccion():
        insight = generate_insight()
        guardar_conclusion()
        respuesta += f"\n\n🔍 {insight}"

    return respuesta


def guardar_memoria_simbolica(texto_usuario, intencion, respuesta):
    archivo = "app/eidos_core/lia_core/memoria_simbolica.json"
    entrada = {
        "fecha": datetime.utcnow().isoformat(),
        "entrada_usuario": texto_usuario,
        "intencion_detectada": intencion,
        "respuesta_generada": respuesta
    }
    memoria = []
     # Guardar en MongoDB
    coleccion = get_collection("memoria")
    coleccion.insert_one(entrada)
    
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            memoria = json.load(f)
    memoria.append(entrada)
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(memoria, f, indent=2, ensure_ascii=False)

         # Revisar si es momento de reflexionar
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