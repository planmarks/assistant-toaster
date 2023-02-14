import datetime
import speech_recognition as sr
import pyttsx3
import random
import toggleSilentMode

def speak(audio, rate=120):
    if toggleSilentMode.is_speaking:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.say(audio)
        engine.runAndWait()

def tell_joke():
    jokes = [
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!"
    ]

    joke = random.choice(jokes)
    if toggleSilentMode.is_speaking:
        speak(joke)
