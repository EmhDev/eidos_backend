import speech_recognition as sr

def transcribir_audio(path_audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(path_audio) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio, language="es-ES")