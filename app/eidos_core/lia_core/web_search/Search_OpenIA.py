#app\eidos_core\lia_core\web_search\Search_OpenIA.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def consultar_openai(pregunta: str) -> str:
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Puedes cambiar a "gpt-4" si tienes acceso
            messages=[
                {"role": "user", "content": pregunta}
            ],
            temperature=0.7
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error consultando OpenAI: {e}"
