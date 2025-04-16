from fastapi import APIRouter, UploadFile, File, Form
from app.audio_processing.Voice_to_text import transcribir_audio
from app.eidos_brain.self_awareness.lia_self import procesar_dialogo
from app.application.services import analizar_con_red_neuronal
from app.audio_processing.Text_to_voice import generar_audio_respuesta
from fastapi.responses import FileResponse
import uuid

router = APIRouter()

@router.post("/analyze")
async def analyze(text: str = Form(None), file: UploadFile = File(None)):
    if text and file is None:
        respuesta = procesar_dialogo(text)
        return {
            "lia_response": respuesta,
            "timestamp": "modo_chat"
        }

    result = analizar_con_red_neuronal(text, file)
    return result

@router.post("/voice")
async def procesar_audio(file: UploadFile = File(...)):
    unique_filename = f"temp_{uuid.uuid4().hex}.wav"

    with open(unique_filename, "wb") as f:
        f.write(await file.read())

    texto = transcribir_audio(unique_filename)
    respuesta = procesar_dialogo(texto)
    audio_path = generar_audio_respuesta(respuesta)

    return FileResponse(audio_path, media_type="audio/mpeg")

@router.post("/analyze-extended")
async def analyze_extended(text: str = Form(...)):
    respuesta = procesar_dialogo_con_busqueda(text)
    return {
        "lia_response": respuesta,
        "timestamp": datetime.utcnow().isoformat()
    }

@router.post("/lia_dialogo")
async def lia_dialogo(text: str = Form(...)):
    respuesta = procesar_dialogo(text)
    return {"lia_response": respuesta}


@router.post("/transfer_consciousness")
async def transfer_consciousness(request: Request):
    data = await request.json()
    texto = data.get("contenido", "")
    
    from app.eidos_brain.self_awareness.lia_self import procesar_dialogo
    respuesta = procesar_dialogo(texto)

    return {
        "respuesta_procesada": respuesta,
        "confirmacion": "Conocimiento recibido por Lía 🌸"
    }