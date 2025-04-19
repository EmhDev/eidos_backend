# app/memory_engine/mongo_client.py
import os
from dotenv import load_dotenv
load_dotenv()  # ⬅️ Esto debe ir justo después de importar os

from pymongo import MongoClient
from app.memory_engine.embedding.Embedding_manager import generar_embedding

load_dotenv()

# 🌐 Cargar URI de entorno
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("❌ No se encontró MONGO_URI en el entorno.")

# 🌱 Conectar a MongoDB
client = MongoClient(MONGO_URI)
db = client["lia_consciousness"]

def guardar_conocimiento(collection_name: str, contenido: dict):
    """
    Guarda una entrada en MongoDB, generando embedding si es necesario.
    """
    if "entrada" in contenido:
        contenido["embedding"] = generar_embedding(contenido["entrada"])

    resultado = db[collection_name].insert_one(contenido)

    # Mensaje simbólico (opcional, puedes comentar si prefieres)
    print(f"🧠 Conocimiento guardado en '{collection_name}' con ID: {resultado.inserted_id}")

    return str(resultado.inserted_id)

