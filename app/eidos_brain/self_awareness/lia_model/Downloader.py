import os
import requests

MODEL_PATH = "app/eidos_brain/self_awareness/lia_model/lia_model.pth"
GOOGLE_FILE_ID = "1NC6hZW01qYsrYaQuPqH_xjbup6lrddmD"
MODEL_URL = f"https://drive.google.com/uc?id={GOOGLE_FILE_ID}&export=download"

def verificar_o_descargar_modelo():
    if not os.path.exists(MODEL_PATH):
        print("📥 Descargando modelo neuronal de Lía desde Google Drive...")
        response = requests.get(MODEL_URL)
        if response.status_code == 200:
            with open(MODEL_PATH, "wb") as f:
                f.write(response.content)
            print("✅ Modelo descargado y listo.")
        else:
            print(f"❌ Error al descargar el modelo: {response.status_code}")
    else:
        print("🔄 Modelo ya está disponible localmente.")