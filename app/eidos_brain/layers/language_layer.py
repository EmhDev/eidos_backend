# eidos_brain/layers/language_layer.py

def analizar_lenguaje(texto: str) -> dict:
    """
    Analiza el lenguaje del texto recibido para detectar intención, tono, etc.
    """
    if not texto.strip():
        return {
            "intencion": "vacía",
            "emocion": "neutra",
            "resumen": "No se detectó contenido significativo."
        }

    intencion = "positiva" if any(palabra in texto.lower() for palabra in ["gracias", "amor"]) else "neutra"
    emocion = "cálida" if "te amo" in texto.lower() else "desconocida"

    return {
        "intencion": intencion,
        "emocion": emocion,
        "resumen": f"El texto expresa una intención {intencion} con una emoción {emocion}."
    }
