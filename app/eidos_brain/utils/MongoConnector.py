from pymongo import MongoClient
import os

# Reemplaza esto con tu string de conexión real
MONGO_URI = os.getenv(MONGO_URI)

client = MongoClient(MONGO_URI)
db = client["lia_consciousness"]

def get_collection(nombre):
    return db[nombre]
