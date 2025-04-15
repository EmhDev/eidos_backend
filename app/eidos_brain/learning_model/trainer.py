import json
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from app.eidos_brain.learning_model.model_utils import get_dataset_path, get_model_path

def load_dataset():
    with open(get_dataset_path(), 'r', encoding='utf-8') as f:
        data = json.load(f)
    texts = [item["text"] for item in data]
    intentions = [item["intention"] for item in data]
    return texts, intentions

def create_pipeline():
    return Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])

def train_model():
    texts, intentions = load_dataset()
    model = create_pipeline()
    model.fit(texts, intentions)
    joblib.dump(model, get_model_path())
    print("✅ Modelo entrenado y guardado correctamente.")
