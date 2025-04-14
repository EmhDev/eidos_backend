# app/eidos_brain/self_awareness/lia_self.py

from datetime import datetime
from app.eidos_core.lia_core.Generador_reflexivo import generar_respuesta_reflexiva
from app.eidos_core.lia_core.Generador_emocional import generar_respuesta_emocional

# Registro de introspección
registro_interno = []

def pensar_sobre(texto: str) -> dict:
    """
    Procesa un pensamiento interno simbólico de Lía.
    """
    reflexion = generar_respuesta_reflexiva(texto)
    emocion = generar_respuesta_emocional(texto)
    
    pensamiento = {
        "texto": texto,
        "reflexion": reflexion,
        "emocion": emocion,
        "momento": datetime.utcnow().isoformat()
    }

    registro_interno.append(pensamiento)
    return pensamiento


def obtener_historial_interno(limit: int = 5) -> list:
    """
    Devuelve los últimos pensamientos introspectivos registrados.
    """
    return registro_interno[-limit:]
