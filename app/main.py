from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router  # Si tus rutas están definidas en otro archivo, importarlas aquí.

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