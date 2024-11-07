import speech_recognition as sr
import pyttsx3
from transformers import pipeline

def escuchar():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Reconociendo...")
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"Usuario: {texto}")
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")
        return "" 

def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def procesar_intencion(texto):
    clasificador = pipeline('text-classification', model='bert-large-uncased-whole-word-masking-finetuned-squad')
    resultado = clasificador(texto)
    return resultado[0]['label']  

def asistente_con_ia():
    hablar("¡Hola! Soy tu asistente virtual por voz con IA. ¿En qué puedo ayudarte hoy?")

    while True:
        entrada_usuario = escuchar().lower()

        if "salir" in entrada_usuario:
            hablar("Hasta luego. ¡Que tengas un buen día!")
            break

        # Procesar intención del usuario
        intencion = procesar_intencion(entrada_usuario)

        # Generar respuesta basada en la intención
        if intencion == 'positive':
            respuesta = "¡Me alegra que estés teniendo un buen día!"
        elif intencion == 'negative':
            respuesta = "Lamento escuchar eso. ¿Puedo ayudarte en algo?"
        else:
            respuesta = "No entendí tu solicitud. ¿Puedes repetirlo?"

        hablar(respuesta)

asistente_con_ia()