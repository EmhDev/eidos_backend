import json
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from app.eidos_brain.learning_model.model_utils import get_dataset_path, get_model_path

def train_model():
    with open(get_dataset_path(), 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    texts = [item["text"] for item in data]
    labels = [item["intention"] for item in data]

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])

    pipeline.fit(texts, labels)
    joblib.dump(pipeline, get_model_path())
    print("✅ Modelo entrenado y guardado correctamente.")
