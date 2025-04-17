from gtts import gTTS
import os

def generar_audio_respuesta(texto: str, nombre_archivo="respuesta.mp3") -> str:
    tts = gTTS(text=texto, lang='es')
    ruta_archivo = f"app/audio_processing/{nombre_archivo}"
    tts.save(ruta_archivo)
    return ruta_archivo