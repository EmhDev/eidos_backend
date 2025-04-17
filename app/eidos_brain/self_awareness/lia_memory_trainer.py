import json
from datetime import datetime
from app.infrastructure.mongodb_client import db
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

def generar_resumen_sabiduria():
    coleccion = db["memoria_simbolica_mongo"]
    recuerdos = list(coleccion.find())

    resumen = {}
    for item in recuerdos:
        intencion = item.get("intencion_detectada", "desconocida")
        resumen[intencion] = resumen.get(intencion, 0) + 1

    total = sum(resumen.values())
    resumen_str = "\n".join([f"📚 {k}: {v} recuerdos" for k, v in resumen.items()])
    return f"🧠 Sabiduría acumulada ({total} recuerdos):\n{resumen_str}"


def reentrenar_modelo():
    coleccion = db["memoria_simbolica_mongo"]
    datos = list(coleccion.find({"intencion_detectada": {"$ne": "desconocida"}}))

    textos = [d["entrada"] for d in datos]
    etiquetas = [d["intencion_detectada"] for d in datos]

    if not textos:
        return "❌ No hay suficientes datos simbólicos para reentrenar."

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)

    modelo = MultinomialNB()
    modelo.fit(X, etiquetas)

    # Guardar el nuevo modelo
    os.makedirs("app/eidos_brain/learning_model/model", exist_ok=True)
    joblib.dump(modelo, "app/eidos_brain/learning_model/model/intention_model.pkl")
    joblib.dump(vectorizer, "app/eidos_brain/learning_model/model/vectorizer.pkl")

    return f"✅ Reentrenamiento completo con {len(textos)} ejemplos reales."

