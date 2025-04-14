# app/eidos_core/input_channel.py

def recibir_input(texto, archivo):
    # De momento solo retornamos un diccionario simbólico
    return {
        "texto": texto,
        "archivo_nombre": archivo.filename if archivo else None,
        "contenido": archivo.file.read() if archivo else None
    }
