import webbrowser
import datetime
import wikipedia
import speech_recognition as sr
import pyttsx3
import commands
import comBrowser
import comOs
import pyautogui
import numpy as np
import cv2
import comCalc
import jokes
import toggleSilentMode

# All systems ready
def speak(audio, rate = 120):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(audio)
    engine.runAndWait()

print('All systems ready.')
speak("All systems ready.")

# Greeting
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
    date = f"{day}/{month}/{year}"
    print(f"{greet} The time is {time} and the date is {date}. Assistant toaster at your command.")
    #speak(f"{greet} The time is {time} and the date is {date}. Assistant toaster at your command.")

wishMe()

def trigger_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    executed = False #Not tested
    while True:
        query = trigger_command().lower()

        if 'open youtube' in query:
            comBrowser.open_youtube()
            executed = True

        if 'open google ads' in query:
            comBrowser.open_google_ads()
            executed = True

        if 'search youtube' in query:
            comBrowser.search_youtube(query.split("search youtube",1)[1])
            executed = True

        if 'search wikipedia' in query:
            comBrowser.search_wikipedia(query.split("search wikipedia",1)[1])
            executed = True

        if 'search bing' in query:
            comBrowser.search_bing(query.split("search bing",1)[1])
            executed = True

        if 'google search' in query:
            comBrowser.search_google(query.split("google search",1)[1])
            executed = True

        if 'hello toaster' in query or 'hi toaster' in query:
            commands.wishMe()
            executed = True

        if "goodbye" in query or "ok bye" in query or "turn off" in query or "that's enough" in query:
            commands.goodbye()
            executed = True
            break

        if 'record speech' in query:
            comOs.record_speech()
            executed = True
        
        if 'empty recycle bin' in query:
            comOs.empty_recycle_bin()
            executed = True

        if 'run directory cleanup' in query:
            comOs.directory_cleanup()
            executed = True
        
        if 'what time is it' in query:
            commands.get_date()
            executed = True

        if 'toaster calculate' in query:
            comCalc.calculate(query)
            executed = True

        if 'set timer for' in query:
            duration = int(query.split("set timer for")[1].split("minutes")[0].strip())
            commands.set_timer(duration)
            print(f"Timer has been set for {duration} minutes.")
            speak(f"Timer has been set for {duration} minutes.")
            executed = True

        if "say a joke" in query or "tell a joke" in query:
            jokes.tell_joke()
            executed = True

        if 'toggle silent mode' in query:
            speak("Turning on silent mode")
            toggleSilentMode.toggle_speaking()
            executed = True

        elif 'silent mode off' in query:
            toggleSilentMode.toggle_speaking()
            speak("Silent mode off")
            executed = True

        #Not tested
        if not executed:
            print("Could not understand your command.")
        else:
            executed = False