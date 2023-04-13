import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Crear un objeto Recognizer
r = sr.Recognizer()

# Crear un objeto gTTS
tts = gTTS(text='Mande... ¿en que le puedo ayudar?', lang='es')

# Guardar la respuesta en un archivo de audio
tts.save('response.mp3')

# Reproducir la respuesta en voz
playsound('response.mp3')

# Escuchar la entrada de voz
with sr.Microphone() as source:
    print("¿En qué puedo ayudarte?")
    audio = r.listen(source)

# Convertir la entrada de voz en texto
command = r.recognize_google(audio, language='es-MX')
print("Tu dijiste: " + command)

if 'abrir archivo' in command:
    # Extraer el nombre del archivo
    filename = command.replace('abrir archivo', '').strip()
    # Abrir el archivo
    os.startfile(filename)

if 'cerrar archivo' in command:
    # Extraer el nombre del archivo
    filename = command.replace('cerrar archivo', '').strip()
    # Cerrar el archivo
    os.system("TASKKILL /F /IM " + filename + ".exe")
    print("Se ha cerrado el archivo " + filename)

# Generar la respuesta en voz
tts = gTTS(text='Hecho', lang='es')
tts.save('response.mp3')
playsound('response.mp3')


'''
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from googlesearch import search

# Crear un objeto Recognizer
r = sr.Recognizer()

# Crear un objeto gTTS
tts = gTTS(text='Mande... ¿en qué le puedo ayudar?', lang='es')

# Guardar la respuesta en un archivo de audio
tts.save('response.mp3')

# Reproducir la respuesta en voz
playsound('response.mp3')

# Escuchar la entrada de voz
with sr.Microphone() as source:
    print("¿En qué puedo ayudarte?")
    audio = r.listen(source)

# Convertir la entrada de voz en texto
command = r.recognize_google(audio, language='es-MX')
print("Tu dijiste: " + command)

# Buscar la respuesta a la pregunta en Google
results = search(command, num_results=1, lang="es")

# Leer la respuesta encontrada en voz alta
if results:
    response = next(results)
    tts = gTTS(text=response, lang='es')
    tts.save('response.mp3')
    playsound('response.mp3')
else:
    tts = gTTS(
        text="Lo siento, no pude encontrar una respuesta a tu pregunta.", lang='es')
    tts.save('response.mp3')
    playsound('response.mp3')


import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Crear un objeto Recognizer
r = sr.Recognizer()

# Crear un objeto gTTS
tts = gTTS(text='Mande... ¿en que le puedo ayudar?', lang='es')

# Guardar la respuesta en un archivo de audio
tts.save('response.mp3')

# Reproducir la respuesta en voz
playsound('response.mp3')

# Escuchar la entrada de voz
with sr.Microphone() as source:
    print("¿En qué puedo ayudarte?")
    audio = r.listen(source)

# Convertir la entrada de voz en texto
command = r.recognize_google(audio, language='es-MX')
print("Tu dijiste: " + command)

# Generar la respuesta en voz
tts = gTTS(text='Entiendo que quieres ' + command, lang='es')
tts.save('response.mp3')
playsound('response.mp3')


import speech_recognition as sr
import pyttsx3
import spacy

# Descarga y carga el modelo de procesamiento de lenguaje natural de spaCy.
nlp = spacy.load('en_core_web_sm')

# Función que convierte texto a voz y reproduce la respuesta.


def respond(text):
    # Crea un objeto motor de texto a voz.
    engine = pyttsx3.init()
    # Define la voz predeterminada.
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    # Convierte el texto en voz y lo reproduce.
    engine.say(text)
    engine.runAndWait()

# Función que escucha el audio del micrófono y devuelve el texto transcribido.


def listen():
    # Crea un objeto reconocedor de voz.
    r = sr.Recognizer()

    # Utiliza el micrófono como fuente de entrada de audio.
    with sr.Microphone() as source:
        print('Listening...')
        # Espera a que el usuario termine de hablar antes de procesar el audio.
        r.pause_threshold = 1
        # Ajusta el nivel de ruido de fondo.
        r.adjust_for_ambient_noise(source, duration=1)
        # Escucha el audio y transcribe el texto.
        audio = r.listen(source)

        try:
            # Transcribe el audio a texto utilizando la API de Google Speech Recognition.
            text = r.recognize_google(audio)
            print(f'You said: {text}')
            return text

        except sr.UnknownValueError:
            print('Sorry, I could not understand what you said.')
            return ''

        except sr.RequestError as e:
            print(f'Speech recognition service error: {e}')
            return ''


# Ciclo de conversación.
while True:
    # Escucha el audio y transcribe el texto.
    text = listen()

    # Procesa el texto utilizando spaCy.
    doc = nlp(text)

    # Determina la respuesta apropiada basada en el texto procesado.
    if 'hello' in text.lower() or 'hi' in text.lower() or 'hey' in text.lower():
        respond('Hello! How can I assist you?')

    elif 'good morning' in text.lower() or 'good day' in text.lower() or 'good afternoon' in text.lower():
        respond('Good morning! How are you today?')

    elif 'what is your name' in text.lower():
        respond('My name is Assistant.')

    elif 'how are you' in text.lower():
        respond('I am doing well, thank you. How about you?')

    else:
        respond('Sorry, I did not understand what you said.')
'''
