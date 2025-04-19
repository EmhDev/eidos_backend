# app/memory_engine/Embedding_manager.py

from sentence_transformers import SentenceTransformer

# Modelo ligero y rápido
modelo_embedding = SentenceTransformer("all-MiniLM-L6-v2")

def generar_embedding(texto: str):
    vector = modelo_embedding.encode(texto)
    return vector.tolist()  # Lo convertimos a lista para guardar en Mongo
