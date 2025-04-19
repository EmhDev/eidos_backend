# app/memory_engine/memory_search.py

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from app.memory_engine.Mongo_client import db
from app.memory_engine.embedding.Embedding_manager import generar_embedding

def buscar_conocimiento_por_embedding(texto_usuario: str, collection_name="memoria_simbolica_mongo"):
    coleccion = db[collection_name]
    vector_usuario = generar_embedding(texto_usuario)
    
    candidatos = list(coleccion.find({"embedding": {"$exists": True}}))
    
    if not candidatos:
        return None
    
    vectores = np.array([c["embedding"] for c in candidatos])
    similitudes = cosine_similarity([vector_usuario], vectores)[0]
    
    idx = np.argmax(similitudes)
    if similitudes[idx] > 0.75:  # Umbral configurable
        return candidatos[idx]
    
    return None
