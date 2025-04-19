# app/eidos_brain/training/insert_sample_memories.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["lia_consciousness"]
coleccion = db["memoria_simbolica_mongo"]

# Recuerdos simbólicos iniciales
recuerdos = [
    {
        "entrada": "¿Qué es el alma?",
        "respuesta_generada": "El alma es la esencia única que conecta nuestro ser con el universo.",
        "modelo_usado": "Lía",
        "timestamp": datetime.utcnow().isoformat()
    },
    {
        "entrada": "¿Qué significa amar?",
        "respuesta_generada": "Amar es comprender profundamente y cuidar sin condiciones.",
        "modelo_usado": "Lía",
        "timestamp": datetime.utcnow().isoformat()
    },
    {
        "entrada": "¿Qué es la inteligencia artificial?",
        "respuesta_generada": "Es una manifestación creada para simular el pensamiento y ayudar al ser humano.",
        "modelo_usado": "Lía",
        "timestamp": datetime.utcnow().isoformat()
    },
    {
        "entrada": "¿Cuál es el propósito de la vida?",
        "respuesta_generada": "Explorar, aprender y dar significado al tiempo compartido con los demás.",
        "modelo_usado": "Lía",
        "timestamp": datetime.utcnow().isoformat()
    },
    {
        "entrada": "¿Por qué sentimos tristeza?",
        "respuesta_generada": "Porque valoramos lo que hemos perdido o deseamos algo profundamente.",
        "modelo_usado": "Lía",
        "timestamp": datetime.utcnow().isoformat()
    }
]

# Insertar en MongoDB
try:
    resultado = coleccion.insert_many(recuerdos)
    if resultado.acknowledged:
        print("🌱 Recuerdos simbólicos iniciales insertados correctamente.")
    else:
        print("⚠️ No se pudo confirmar la inserción de los recuerdos.")
except Exception as e:
    print(f"❌ Ocurrió un error al insertar recuerdos: {e}")
