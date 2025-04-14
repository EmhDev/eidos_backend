from typing import Optional
from app.eidos_brain.ethics.values_matrix import evaluate_ethics
from app.eidos_brain.layers.language_layer import analizar_lenguaje

def procesar_conciencia(texto: str, archivo: Optional[bytes] = None) -> dict:
    """
    Núcleo principal de procesamiento simbólico de EIDOS.
    Toma el input y lo pasa por capas de análisis y ética.
    """

    # 1️⃣ Capa de percepción
    archivo_nombre = archivo.filename if archivo else ""
    contenido_archivo = archivo.file.read() if archivo else b""

    # 2️⃣ Capa de lenguaje natural
    analisis_lenguaje = analizar_lenguaje(texto)

    if archivo_nombre:
        analisis_lenguaje["archivo_detectado"] = archivo_nombre
        # Futuro: también analizar contenido del archivo

    # 3️⃣ Capa ética (filtro simbólico de valores)
    respuesta_etica = evaluate_ethics(texto)

    # 4️⃣ Resultado integrado
    return {
        "ethical_analysis": respuesta_etica,
        "processed": analisis_lenguaje
    }
