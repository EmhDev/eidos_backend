from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="EIDOS - Sistema de Protección Ética")

app.include_router(router)
