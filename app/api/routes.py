from fastapi import APIRouter, UploadFile, File, Form
from app.audio_processing.Voice_to_text import transcribir_audio
from app.eidos_core.lia_core.Respuesta_consciente import generar_respuesta_consciente
from app.application.services import analizar_con_red_neuronal
from app.audio_processing.Text_to_voice import generar_audio_respuesta
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/analyze")
async def analyze(text: str = Form(None), file: UploadFile = File(None)):
    if text and file is None:
        respuesta = generar_respuesta_consciente(text)
        return {
            "lia_response": respuesta,
            "timestamp": "modo_chat"
        }

    result = analizar_con_red_neuronal(text, file)
    return result

import uuid
from fastapi.responses import FileResponse

@router.post("/voice")
async def procesar_audio(file: UploadFile = File(...)):
    unique_filename = f"temp_{uuid.uuid4().hex}.wav"

    with open(unique_filename, "wb") as f:
        f.write(await file.read())

    texto = transcribir_audio(unique_filename)
    respuesta = generar_respuesta_consciente(texto)
    audio_path = generar_audio_respuesta(respuesta)

    return FileResponse(audio_path, media_type="audio/mpeg")
