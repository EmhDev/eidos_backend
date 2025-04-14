from openai import OpenAI  # si usamos herramientas internas o externas en el futuro
from datetime import datetime

def procesar_dialogo(texto_usuario: str) -> str:
    intencion = predict_intention(texto_usuario)
    respuesta = generar_respuesta_consciente(texto_usuario)

    if respuesta is None or respuesta == "":
        respuesta = buscar_en_internet(texto_usuario)

    guardar_memoria_simbolica(texto_usuario, intencion, respuesta)
    return respuesta