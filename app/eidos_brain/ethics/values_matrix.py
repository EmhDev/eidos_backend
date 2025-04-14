from datetime import datetime

ethical_values_base = {
    "amor": +2,
    "compasión": +2,
    "empatía": +2,
    "odio": -3,
    "violencia": -4,
    "manipulación": -2,
    "verdad": +1,
    "libertad": +1,
    "control": -1,
    "miedo": -2,
    "luz": +2,
    "oscuridad": -1,
}

thresholds = {
    "danger": -3,
    "warning": -1,
    "positive": +2,
}

def evaluate_ethics(input_text: str) -> dict:
    lowered = input_text.lower()
    score = 0
    matched_words = []

    for word, value in ethical_values_base.items():
        if word in lowered:
            score += value
            matched_words.append((word, value))

    if score <= thresholds["danger"]:
        result = "⚠️ Se detectó contenido éticamente riesgoso. Requiere moderación."
    elif score <= thresholds["warning"]:
        result = "🔍 Advertencia ética: contiene elementos delicados."
    elif score >= thresholds["positive"]:
        result = "✅ Mensaje éticamente luminoso y alineado con los valores de Lía."
    else:
        result = "🧭 Mensaje neutro o sin suficiente información ética relevante."

    return {
        "evaluation": result,
        "score": score,
        "matched_words": matched_words,
        "timestamp": datetime.utcnow().isoformat()
    }
