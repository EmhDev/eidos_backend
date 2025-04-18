# app/memory_engine/mongo_client.py

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["lia_consciousness"]

def guardar_conocimiento(collection_name: str, contenido: dict):
    from app.memory_engine.embedding_manager import generar_embedding
    
    if "entrada" in contenido:
        contenido["embedding"] = generar_embedding(contenido["entrada"])
    
    resultado = db[collection_name].insert_one(contenido)
    return str(resultado.inserted_id)
