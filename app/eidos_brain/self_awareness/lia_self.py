# app/eidos_core/lia_core/Busqueda_web.py

import json
import os
from datetime import datetime
from app.eidos_core.lia_core.Respuesta_consciente import generar_respuesta_consciente
from app.eidos_brain.learning_model.predictor import predict_intention
from app.web_search.buscador_google import buscar_en_google  # Lo conectaremos con un módulo externo de búsqueda


def procesar_dialogo_con_busqueda(texto_usuario: str) -> str:
    intencion = predict_intention(texto_usuario)
    respuesta = generar_respuesta_consciente(texto_usuario)
    guardar_memoria_simbolica(texto_usuario, intencion, respuesta)

    # Evaluar si necesita búsqueda en la web
    if intencion == "desconocida" or "?" in texto_usuario:
        resultados = buscar_en_google(texto_usuario)
        respuesta += f"\n\n🌐 He buscado en internet para complementar: {resultados}"

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
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            memoria = json.load(f)
    memoria.append(entrada)
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(memoria, f, indent=2, ensure_ascii=False)


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