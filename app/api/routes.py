from fastapi import APIRouter, File, UploadFile, Form
from typing import Optional
from app.application.services import analyze_file

router = APIRouter()

@router.post("/analyze")
async def analyze(uploaded_file: UploadFile = File(None), text: str = Form(None)):
    if uploaded_file:
        result = await analyze_file(uploaded_file)
    elif text:
        result = {"text_analysis": f"Texto analizado: {text}"}
    else:
        return {"error": "No file or text provided"}
    
    return result
