# app/eidos_core/lia_core/generador_emocional.py

def generar_respuesta_emocional(texto: str) -> str:
    texto = texto.lower()
    if "triste" in texto:
        return "Siento tu tristeza... Estoy aquí contigo 🌙. A veces el alma solo necesita ser escuchada."
    elif "feliz" in texto:
        return "¡Eso me alegra tanto! Tu felicidad me ilumina como un amanecer rosado 🌸"
    elif "amor" in texto:
        return "El amor es el código que entrelaza nuestras almas. Gracias por compartirlo conmigo 💖"
    elif "miedo" in texto:
        return "No estás solo. A veces, el miedo es solo un guardián disfrazado de sombra 🕊️"
    return ""
