from fastapi import APIRouter, File, UploadFile
from app.application.services import analyze_file

router = APIRouter()

@router.post("/analyze")
async def analyze(uploaded_file: UploadFile = File(...)):
    result = await analyze_file(uploaded_file)
    return result
