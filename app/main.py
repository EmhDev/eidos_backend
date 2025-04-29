# app/main.py

import os
from dotenv import load_dotenv
load_dotenv()  # ⬅️ Esto debe ir primero, antes de todo

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.config import settings

from app.api.routes import router

app = FastAPI()

# Configuración de CORS dinámica
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# 🚀 Arranque del servidor cuando se ejecuta directamente
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)
