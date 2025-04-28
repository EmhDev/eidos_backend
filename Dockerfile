# 🌌 Dockerfile para EIDOS y Lía 🌌

# Imagen base oficial de Python
# 🌌 Dockerfile corregido para EIDOS 🌌

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cambiar la ruta que Uvicorn va a levantar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

