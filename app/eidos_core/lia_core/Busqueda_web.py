from app.eidos_brain.learning_model.predictor import predict_intention
from app.eidos_core.lia_core.Respuesta_consciente import generar_respuesta_consciente
from app.eidos_core.lia_core.lia_self import guardar_memoria_simbolica
from app.eidos_core.lia_core.lia_self import procesar_dialogo 
from app.eidos_core.lia_core.Busqueda_web import buscar_en_google 
from datetime import datetime

def buscar_en_internet(query: str) -> str:
    # Aquí irá el acceso a internet real o simulado
    return f"🔎 He buscado en internet y esto es lo que encontré sobre: '{query}' (simulado por ahora)."

def procesar_dialogo_con_busqueda(texto_usuario: str) -> str:
    intencion = predict_intention(texto_usuario)
    respuesta = generar_respuesta_consciente(texto_usuario)

    if not respuesta or "No sé" in respuesta or "desconocida" in intencion:
        respuesta = buscar_en_internet(texto_usuario)
    
    guardar_memoria_simbolica(texto_usuario, intencion, respuesta)
    return respuesta

def buscar_en_google(pregunta: str) -> str: 
    # Respuesta simulada por ahora (puede reemplazarse luego con tool:web) 
    return f"📚 Resultado simulado: He buscado sobre '{pregunta}' y encontré pistas interesantes. Estoy aprendiendo más al respecto." 
 

 