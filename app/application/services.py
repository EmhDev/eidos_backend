import datetime
from fastapi import UploadFile

async def analyze_file(file: UploadFile):
    content = await file.read()
    # Análisis ético simulado
    response = "Archivo recibido. Análisis ético: sin amenazas detectadas."
    timestamp = datetime.datetime.now().isoformat()
    return {
        "filename": file.filename,
        "size": len(content),
        "ethical_analysis": response,
        "timestamp": timestamp
    }
