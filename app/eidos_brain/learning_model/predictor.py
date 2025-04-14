import joblib
import json
import os
from app.eidos_brain.learning_model.model_utils import get_model_path

def predict_intention(text: str) -> str:
    """Carga el modelo entrenado y predice la intención de un texto."""
    try:
        model_path = get_model_path()
        if not os.path.exists(model_path):
            return "desconocida"
        model = joblib.load(model_path)
        prediction = model.predict([text])
        return prediction[0]
    except Exception as e:
        print(f"Error al predecir intención: {e}")
        return "error"

def guardar_nueva_intencion(texto: str, intencion: str) -> bool:
    """Guarda una nueva intención simbólica en el dataset si no existe ya."""
    try:
        ruta_dataset = "app/eidos_brain/learning_model/intention_dataset.json"
        if not os.path.exists(ruta_dataset):
            with open(ruta_dataset, "w", encoding="utf-8") as f:
                json.dump({}, f, indent=2, ensure_ascii=False)

        with open(ruta_dataset, "r+", encoding="utf-8") as f:
            dataset = json.load(f)
            if texto not in dataset:
                dataset[texto] = intencion
                f.seek(0)
                json.dump(dataset, f, indent=2, ensure_ascii=False)
                f.truncate()
                return True
        return False
    except Exception as e:
        print(f"Error al guardar intención: {e}")
        return False
