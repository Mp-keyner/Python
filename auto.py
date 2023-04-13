'''
    Description: Create your own virtual assistant with python.
    Author: aulerjbailey
    Version: 1.0.0
    Video: https://youtu.be/8WKjX0dbh4E
import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

# name of the virtual assistant
name = 'auto'

# your api key
key = 'YOUR_API_KEY_HERE'

# the flag help us to turn off the program
flag = 1

listener = sr.Recognizer()

engine = pyttsx3.init()

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)


def talk(text):
    
        here, virtual assistant can talk
    
    engine.say(text)
    engine.runAndWait()


def listen():
   
        The program recover our voice and it sends to another function
 
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()

            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk("Vuelve a intentarlo, no reconozco: " + rec)
    except:
        pass
    return flag


def run(rec):
   
        All the actions that virtual assistant can do
    
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    elif 'cuantos suscriptores tiene' in rec:
        name_subs = rec.replace('cuantos suscriptores tiene', '')
        data = urllib.request.urlopen(
            f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={name_subs.strip()}&key={key}').read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs + " tiene {:,d}".format(int(subs)) + " suscriptores!")
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'exit' in rec:
        flag = 0
        talk("Saliendo...")
    else:
        talk("Vuelve a intentarlo, no reconozco: " + rec)
    return flag


while flag:
    flag = listen()

Keyopanei = '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'

listener = sr.Recognizer()

try:
    with sr.Microphone() as sourse:
        print("Escuchando...")
        voice = listener.listen(sourse)
        rec = listener.recognize_google(voice)
        print(rec)
except:
    pass



# *****************************************************************************************************
# *****************************************************************************************************
# *************************** CODIGO CREADO Y COMPARTIDO POR LKTECHAI *********************************
# *****************************************************************************************************
# *****************************************************************************************************

# Las librerias deben importarse desde la consola o desde linea de comnado ejecutando pip install <libreria>
import speech_recognition as sr
import openai
from gtts import gTTS
from pygame import mixer
import pyttsx3  # Si la libreria gTTS no funciona se puede utilizar esta que es la mas utilizada
import os
import time as ti
import random


openai.api_key = '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'


# Definimos la funcion que transforma la voz captada en el mic a texto
def transformar_audio_a_texto():

    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("Ya puedes hablar!")
        audio = r.listen(origen)
        try:
            # Se debe especificar el lenguaje con el que se reconoce la voz
            pedido = r.recognize_google(audio, language="es")
            print("You: " + pedido)
            return pedido

        except sr.UnknownValueError:
            print("Ups, no entendi!")
            return "Sigo esperando"

        except sr.RequestError:
            print("Ups, no hay servicio!")
            return "Sigo esperando"

        except:
            print("Ups, algo salio mal!")
            return "Sigo esperando"


# Definimos la funcion que va a transformar el texto (mensaje) en audio, dejo tanto para libreria gTTS como para pyttsx3
def hablar(mensaje):
    # ******* Esta seccion de codigo es para libreria gTTS ********
    volume = 0.7
    tts = gTTS(mensaje, lang="es", slow=False)
    ran = random.randint(0, 9999)
    filename = 'Temp' + format(ran) + '.mp3'
    tts.save(filename)
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(volume)
    mixer.music.play()

    while mixer.music.get_busy():
        ti.sleep(0.3)

    mixer.quit()
    os.remove(filename)

    # ******* Esta seccion de codigo es para libreria pyttsx3, solo utilizar una quitando el numeral ********
    # En caso de que la libreria gTTS no funcione
    # Encender el motor de pyttsx3
    # engine = pyttsx3.init()
    # Bajar velocidad de reproduccion, por defecto es 200
    # engine.setProperty('rate', 150)

    # Pronunciar mensaje
    # engine.say(mensaje)
    # engine.runAndWait()


def main():
    conversation = ""

    hablar("Hola! Soy Auto tu asistente personal, ¿en que puedo ayudarte?")

    while True:
        question = transformar_audio_a_texto().lower()

        conversation += "\nYou: " + question + "\nVicky:"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=conversation,
            temperature=0.5,
            max_tokens=100,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["\n", " You:", " Auto:"]
        )
        answer = response.choices[0].text.strip()
        conversation += answer
        print("Auto: " + answer + "\n")
        hablar(answer)


main()

import openai_secret_manager
import openai
import pyttsx3

# Obtener las credenciales de OpenAI desde el Secret Manager de Google Cloud
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

# Inicializar el cliente de OpenAI
openai.api_key = secrets['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']

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Establecer la voz en español
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)  # voz en español de España

# Configurar la velocidad de habla
engine.setProperty('rate', 150)

# Función para hacer una consulta a la API de OpenAI


def ask_openai(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer

# Función para que el asistente responda en voz alta


def say(text):
    engine.say(text)
    engine.runAndWait()


# Esperar a que el usuario hable
with sr.Microphone() as source:
    print("Dime, ¿en qué puedo ayudarte?")
    audio = listener.listen(source)

# Obtener el texto hablado por el usuario
try:
    text = listener.recognize_google(audio, language="es-ES")
    print(f"Usuario: {text}")
except sr.UnknownValueError:
    text = ""
    print("Lo siento, no te he entendido.")
except sr.RequestError:
    text = ""
    print("Lo siento, ha ocurrido un error al procesar tu solicitud.")

# Si el usuario ha dicho algo, hacer una consulta a OpenAI y obtener la respuesta
if text:
    answer = ask_openai(text)
    if answer:
        print(f"Asistente: {answer}")
        say(answer)
    else:
        print("Lo siento, no tengo una respuesta para esa pregunta.")
else:
    print("No has dicho nada, ¿en qué puedo ayudarte?")


import openai
import pyttsx3
import speech_recognition as sr

# Configuración de la API de OpenAI
openai.api_key = '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'

# Configuración del motor de texto a voz
engine = pyttsx3.init()

# Configuración del reconocimiento de voz
r = sr.Recognizer()

# Función que convierte texto a voz


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Función que reconoce voz y retorna el texto


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
        print(text)
        return text.lower()

# Función que realiza la consulta a OpenAI


def openai_query(query):
    response = openai.Completion.create(
        engine="davinci",
        prompt=query,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[1].text.strip()


# Inicio del asistente
speak("Hola, ¿en qué puedo ayudarte?")


while True:
    try:
        text = listen()
        if "adiós" in text:
            speak("Hasta luego, ¡que tengas un buen día!")
            break
        else:
            response = openai_query(text)
            speak(response)
    except Exception as e:
        print(e)
        speak("Lo siento, no pude entenderte.")

import openai
import pyttsx3

# Configuración de la API
openai.api_key = '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'

# Configuración del motor de síntesis de voz
engine = pyttsx3.init()

# Función para obtener la respuesta a una pregunta


def get_openai_response(question):
    # Formulamos la pregunta a la API de OpenAI
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Answer the following question: {question}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Obtenemos la respuesta de la API
    answer = response.choices[0].text.strip()
    return answer

# Función para sintetizar la respuesta


def speak(response):
    engine.say(response)
    engine.runAndWait()


# Ejemplo de uso
question = "¿Cuál es la capital de Francia?"
answer = get_openai_response(question)
speak(answer)


import openai
import openai_secret_manager

# Autenticación con la API de OpenAI
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

openai.api_key = secrets["api_key"]

# Función para hacer consultas a la API de OpenAI
def ask_question(question):
    response = openai.Completion.create(
        engine="davinci",  # Modelo de lenguaje a utilizar
        prompt=f"Answer the following question:\n{question}\nAnswer:",
        temperature=0.5,  # Controla la creatividad de las respuestas
        max_tokens=1024,  # Número máximo de palabras en la respuesta
    )
    return response.choices[0].text.strip()

'''
import openai

# establece la clave de API
openai.api_key = "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"


def Pregunta(question):
    # establece el motor del modelo a utilizar y el idioma
    model_engine = "davinci"
    # establece el prompt
    prompt = f"Responder a la siguiente pregunta:\n\n{question}\n\nRespuesta:"

    # llama la API de OpenAI para generar una respuesta
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # obtiene la respuesta del modelo y la retorna
    answer = response.choices[0].text.strip()
    return answer


# pregunta algo
duda = str(input("Ingresa una pregunta: "))
question = f"{duda}?"
answer = Pregunta(question)

# muestra la respuesta por consola
print(f"Q: {question}")
print(f"A: {answer}")
