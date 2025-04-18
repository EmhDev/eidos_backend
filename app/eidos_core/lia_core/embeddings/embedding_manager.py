from sentence_transformers import SentenceTransformer
import numpy as np

# Cargamos el modelo liviano
modelo_embedding = SentenceTransformer("all-MiniLM-L6-v2")

def generar_embedding(texto: str):
    vector = modelo_embedding.encode(texto)
    return vector.tolist()  # Lo pasamos a lista para guardar en Mongo
