import pyttsx3
import speech_recognition as sr
import subprocess as sp
from datetime import datetime
import pywhatkit
import pyautogui
import wikipedia
import smtplib
import webbrowser as wb
import chistesESP as chistes

voice = pyttsx3.init('sapi5')
voices = voice.getProperty('voices')
# print(voices[1].id)
voice.setProperty('voice', voices[0].id)
voice.setProperty('rate', 140)

def speak(text):
    voice.say(text)
    voice.runAndWait()

def welcome():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Buenos dias!')
    elif hour >= 12 and hour < 18:
        speak('Buenas tardes!')
    else:
        speak('Buenas noches!')
    speak('Mi nombre es Percy y soy su asistente virtual. Por favor dime como puedo ayudarte, si necesitas saber todos mis comandos di ayuda')

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Te escucho!')
        audio = recognizer.listen(source, phrase_time_limit=3)
    try:
        command = recognizer.recognize_google(audio, language='es-MX')
        print(f'Creo que dijiste "{command}"')
        command = command.lower()
        command = command.split(' ')
    except:
        print('No entiendo')
        return "None"
    return command

if __name__ == "__main__":
    welcome()
    while True:
        command = takeCommand()
        if 'percy' in command or 'computadora' in command or 'compu' in command or 'pc' in command:
            if 'abre' in command or 'abrir' in command:
                sites={
					'google':'google.com',
					'youtube':'youtube.com',
					'instagram':'instagram.com'
				}
                for i in list(sites.keys()):
                    if i in command:
                        sp.call(f'start chrome.exe {sites[i]}', shell=True)
                        speak(f'Abriendo {i}')

            elif 'hora' in command:
                time = datetime.now().strftime('%H:%M %p')
                speak(f'Son las {time}')

            elif 'fecha' in command:
                fecha = datetime.now().strftime('%d-%h-%Y')
                speak('La fecha es: ' + str(fecha))

            elif 'día' in command:
                dia = datetime.now().strftime('%d')
                speak('Hoy es el día ' + str(dia))

            elif 'mes' in command:
                mes = datetime.now().strftime('%B')
                mes_translate = spanish_month[mes]
                speak('Estamos en el mes de ' + str(mes_translate))

            elif 'año' in command:
                year = datetime.now().strftime('%Y')
                speak('Estamos en el ' + str(year))

            elif 'wikipedia' in command:
                query = command.replace('wikipedia', '')
                speak(f'buscando en wikipedia {query}')
                result = wikipedia.set_lang('es')
                result = wikipedia.summary(query, sentences=3)
                speak(result)

            elif 'reproduce' in command:
                sound = command.replace("reproduce", '')
                speak(f'reproduciendo {sound}')
                pywhatkit.playonyt(sound)

            elif 'pantalla' in command:
                screenshot = pyautogui.screenshot()
                screenshot.save('Screenshot.png')
                speak('Capturando la pantalla')

            elif 'busca en google' in command:
                consulta = recognizer.replace('busca en google', '')
                speak('Buscando en google' + consulta)
                pywhatkit.search(consulta)

            elif 'chiste' in command:
                chiste = chistes.get_random_chiste()
                speak(chiste)

            elif 'adios' in command or 'terminar' in command or 'stop' in command:
                speak('Sesion finalizada')
                quit()
