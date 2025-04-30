# 🌌 Dockerfile para EIDOS y Lía 🌌
# Imagen base oficial de Python
#STANDAR POSIX
# Con configuraciones dinámicas desde build_config.env

# 🌌 Dockerfile final para EIDOS - Lía 🌌
# Backend en FastAPI con configuraciones de build dinámicas

FROM python:3.12-slim

WORKDIR /app

# Copiamos archivos necesarios primero
COPY requirements.txt .
COPY build_config.env .

# Actualizamos pip
RUN python -m pip install --upgrade pip

# Definimos las variables de entorno para instalación
ENV PIP_TIMEOUT=580
ENV PIP_RETRIES=5

# Instalamos dependencias usando las variables
RUN pip install --no-cache-dir --retries $PIP_RETRIES --timeout $PIP_TIMEOUT -r requirements.txt

# Copiamos el resto de la app
COPY . .

# Declaramos el puerto que usará FastAPI
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]