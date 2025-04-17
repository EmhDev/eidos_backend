# app/main.py
import sys
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://cleanmind-frontend.onrender.com"],  # ⚠️ el origen de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar las rutas
app.include_router(router)