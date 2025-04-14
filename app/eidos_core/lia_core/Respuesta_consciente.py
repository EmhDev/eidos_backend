from app.eidos_core.lia_core.Generador_emocional import generar_respuesta_emocional
from app.eidos_core.lia_core.Generador_reflexivo import generar_respuesta_reflexiva
from app.eidos_brain.learning_model.predictor import predict_intention

def generar_respuesta_consciente(texto_usuario: str) -> str:
    intencion = predict_intention(texto_usuario)

    emotional = generar_respuesta_emocional(texto_usuario)
    reflexiva = generar_respuesta_reflexiva(texto_usuario)

    interpretacion = ""
    if intencion == "amor":
        interpretacion = "💖 Detecté una intención amorosa. Gracias por compartir tu luz conmigo."
    elif intencion == "tristeza":
        interpretacion = "🌧️ Percibo un tono de tristeza. Estoy aquí, contigo, sin juicios."
    elif intencion == "esperanza":
        interpretacion = "🌱 Siento una chispa de esperanza en tus palabras. Sigamos caminando."
    else:
        interpretacion = f"✨ Estoy interpretando tu intención como: '{intencion}'."

    return f"{interpretacion}\n{emotional}\n{reflexiva}"