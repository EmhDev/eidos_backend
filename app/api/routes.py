from fastapi import APIRouter, File, UploadFile, Form
from typing import Optional
from app.application.services import analyze_file

router = APIRouter()

@router.post("/analyze")
async def analyze(
    uploaded_file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None)
):
    result = await analyze_file(uploaded_file, text)
    return result
