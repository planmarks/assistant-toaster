import speech_recognition as sr
import pyttsx3

is_speaking = True

def speak(audio, rate=120):
    global is_speaking
    if is_speaking:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.say(audio)
        engine.runAndWait()
    else:
        return

def toggle_speaking():
    global is_speaking
    if is_speaking:
        is_speaking = False
        print("Silent mode on")
    else:
        is_speaking = True
        print("Silent mode off")
        speak("Silent mode off")
