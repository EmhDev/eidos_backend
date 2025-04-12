from fastapi import UploadFile, File, Form
from app.application.services import analizar_con_red_neuronal

@router.post("/analyze")
async def analyze(text: str = Form(...), file: UploadFile = File(None)):
    result = analizar_con_red_neuronal(text, file)
    return result