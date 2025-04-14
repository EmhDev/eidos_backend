from app.eidos_brain.core import procesar_conciencia
import json
import datetime

def analizar_con_red_neuronal(texto, archivo):
    resultado = procesar_conciencia(texto, archivo)

    resumen_etico = resultado.get("ethics", {}).get("evaluación", "Sin resultado ético.")
    resumen_lenguaje = resultado.get("language_analysis", {}).get("resumen", "")

    return {
        "ethical_analysis": f"{resumen_etico}\n{resumen_lenguaje}",
        "timestamp": datetime.datetime.now().isoformat()
    }