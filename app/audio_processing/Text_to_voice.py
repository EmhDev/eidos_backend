from gtts import gTTS

def generar_audio_respuesta(texto: str) -> str:
    tts = gTTS(text=texto, lang="es")
    output_path = "respuesta_lia.mp3"
    tts.save(output_path)
    return output_path
