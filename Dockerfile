# 🌟 Dockerfile para desplegar EIDOS y Lía 💖

# Usar imagen oficial de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Cargar las variables de entorno si están
# (La app debe manejar .env con load_dotenv en el código)

# Exponer el puerto que usará FastAPI
EXPOSE 8000

# Comando para arrancar la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
