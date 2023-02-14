import datetime
import time
import speech_recognition as sr
import pyttsx3
import toggleSilentMode
import winsound

def speak(audio, rate=120):
    if toggleSilentMode.is_speaking:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.say(audio)
        engine.runAndWait()

def wishMe():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year
    if hour >= 0 and hour < 12:
        greet = "Good morning sir."
    elif hour >= 12 and hour < 18:
        greet = "Good afternoon sir."
    elif hour >= 18 and hour < 24:
        greet = "Good night sir."
    time = f"{hour}:{minute}"
    date = f"{month}/{year}"
    print(f"{greet} The time is {time} and the date is {date}. Assistant toaster at your command.")
    speak(f"{greet} The time is {time} and the date is {date}. Assistant toaster at your command.")

    speak(greet)
    print(greet)
    print(f"Time: {time}")
    print(f"Date: {date}")

def goodbye():
    speak("Okay. Good bye sir.")

def get_date():
    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%I:%M %p")
    date_string = current_time.strftime("%A, %B %d")
    speak(f"The time is {time_string} on {date_string}")

def set_timer(duration):
    print(f"Timer set for {duration} minutes.")
    time.sleep(duration * 60)
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    print("Timer is done.")
    speak("Timer is done.")
