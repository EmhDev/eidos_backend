from app.eidos_core.lia_core.Busqueda_web import buscar_en_internet

def generar_respuesta_consciente(texto_usuario: str) -> str:
    emotional = generar_respuesta_emocional(texto_usuario)
    reflexiva = generar_respuesta_reflexiva(texto_usuario)

    if "desconocida" in emotional or "?" in texto_usuario:
        extra_info = buscar_en_internet(texto_usuario)
        return f"{emotional}\n{reflexiva}\n\n{extra_info}"

    return f"{emotional}\n{reflexiva}"