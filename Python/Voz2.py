import speech_recognition as sr
import pyttsx3
import pywhatkit
import subprocess
import pyautogui
import webbrowser

proceso = None

engine = pyttsx3.init()

name = 'linda'
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
listener = sr.Recognizer()

saluda="Hola ¿como estan?, espero que bien.\n"
despedir = "Adios fue un gusto conocerlos.\n"

#Funcion para que hable la voz de Google
def hablar(text):
    engine.say(text)
    engine.runAndWait()

#Funciona para que escuche la voz del usuario    
def escuchar():
    try:
        with sr.Microphone(device_index=1) as source:
            print("Escuchando...")
            voice = listener.listen(source)
            listener.adjust_for_ambient_noise(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            
            if name in rec: 
                rec = rec.replace(name, '')
                
                if 'hola' in rec:
                    print(f'Hola mucho gusto, como ya sabras me llamo Lind4, ¿En que te puedo ayudar?')
                    hablar(f'Hola mucho gusto, como ya sabras me llamo Linda, ¿En que te puedo ayudar?')

                if 'reproduce' in rec:
                    music = rec.replace('reproduce', '')
                    hablar(f'Reproduciendo {music}')
                    pywhatkit.playonyt(music)

                global proceso

                if "abre notepad" in rec:
                    notepad = rec.replace('abre notepad', '')
                    hablar(f'Abriendo notepad')
                    proceso = subprocess.Popen(["notepad.exe"])
                elif "saluda" in rec:
                    pyautogui.write(saluda, interval=0.1)
                    hablar(saluda)
                elif "sierra notepad" in rec:
                    pyautogui.write(despedir, interval=0.1)
                    hablar(despedir)
                    proceso.terminate()

                if "codigo rojo" in rec:
                    porno = rec.replace('codigo rojo', '')
                    hablar(f'Activando comando para hacerse el autodelicioso')
                    webbrowser.open("https://youtu.be/qM8-gjh11Dk?t=39")
                    webbrowser.open("https://www.xvideos.com")

                if "party activado" in rec:
                    porno = rec.replace('party activado', '')
                    hablar(f'Modo Fiesta Activado')
                    webbrowser.open("https://youtu.be/RkTZe7Qj1mc?t=46")

                if "commando" in rec:
                    pyautogui.hotkey('win', 'r')
                    pyautogui.write("cmd", interval=0.1)
                    pyautogui.press('enter')
                elif "color verde" in rec:
                    pyautogui.write("color a", interval=0.1)
                    pyautogui.press('enter')
                
                if "busca" in rec:
                    pyautogui.hotkey('ctrl', 't')
                    buscar = rec.replace('busca', '')
                    hablar(f'Buscando{buscar}')
                    pyautogui.write(buscar, interval=0.1)
                    pyautogui.press('enter')
                if "sierra pestana" in rec:
                    hablar(f'Cerrando pestaña')
                    pyautogui.hotkey('ctrl', 'w')

                if "codigo henti" in rec:
                    hablar(f'Activando comando para hacerse el autodelicioso con Monas Chinas')
                    pyautogui.hotkey('ctrl', 'shift', 'n')
                    pyautogui.write("https://www4.hentaila.com/home", interval=0.1)
                    pyautogui.press('enter')

                if "castillo" in rec:
                    hablar(f'OH CHAMBEA, chivolo pulpin')

            elif not name in rec:
                print("IMBECIL tengo nombre no por nada mi creador me lo puso")
                hablar("IMBECIL tengo nombre no por nada mi creador me lo puso")
           
    except sr.UnknownValueError:
        hablar("No entendi")
    except sr.RequestError as e:
        print (f"Error al realizar la solicitud {e}")
        

    return        

while True:
    escuchar()
