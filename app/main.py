# app/main.py
import sys
import os

# Aseguramos que el directorio 'app' esté en el PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router  # Esto debería funcionar ahora

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://cleanmind-1.onrender.com"],  # Agrega la URL de tu frontend aquí
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar las rutas
app.include_router(router)