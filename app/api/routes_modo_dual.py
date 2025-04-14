
from fastapi import APIRouter, UploadFile, File, Form
from app.application.services import analizar_con_red_neuronal
from app.eidos_core.lia_core import generar_chat_estilo_lia

router = APIRouter()

@router.post("/analyze")
async def analyze(text: str = Form(...), file: UploadFile = File(None)):
    if file is None and text:
        # Modo chat libre de Lía
        respuesta = generar_chat_estilo_lia(text)
        return {
            "modo": "chat",
            "respuesta": respuesta,
            "timestamp": "✨ generado por Lía"
        }
    else:
        # Modo análisis ético
        result = analizar_con_red_neuronal(text, file)
        result["modo"] = "analisis"
        return result
