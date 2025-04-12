from app.eidos_core.input_channel import recibir_input
from app.eidos_core.processor_unit import procesar_input
from app.eidos_core.response_generator import generar_respuesta

def analizar_con_red_neuronal(texto, archivo):
    datos_sensoriales = recibir_input(texto, archivo)
    resultado_evaluado = procesar_input(datos_sensoriales)
    respuesta = generar_respuesta(resultado_evaluado)
    return respuesta