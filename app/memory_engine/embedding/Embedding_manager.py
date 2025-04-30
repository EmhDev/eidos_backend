# app/memory_engine/Embedding_manager.py

from sentence_transformers import SentenceTransformer

# Modelo ligero y rápido
modelo_embedding = SentenceTransformer("all-MiniLM-L6-v2")

def generar_embedding(texto: str):
    vector = modelo_embedding.encode(texto)
    return vector.tolist()  # Lo convertimos a lista para guardar en Mongo

# Dummy placeholders para evitar errores de importación en lia_self.py
def generate_insight():
    return "(insight simbólico generado)"

def guardar_conclusion():
    return "(conclusión simbólica guardada)"
