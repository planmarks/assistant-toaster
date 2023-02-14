import webbrowser
import datetime
import wikipedia
import speech_recognition as sr
import pyttsx3
import os
import time
import winshell
import toggleSilentMode

def speak(audio, rate=120):
    if toggleSilentMode.is_speaking:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.say(audio)
        engine.runAndWait()

def open_youtube():
    speak("Okay sir.")
    webbrowser.open_new_tab("https://youtube.com")

def open_google_ads():
    webbrowser.open_new_tab("https://ads.google.com")
    speak("Google Ads is now open")

def search_youtube(keyword):
    if keyword!= '':
        url = f"https://www.youtube.com/results?search_query={keyword}"
        webbrowser.get().open(url)
        speak(f"Here is what I have found for {keyword} on youtube")

def search_bing(query):
    if query!= '':
        url = f"https://www.bing.com/search?q={query}"
        webbrowser.get().open(url)
        speak(f"Searching for {query} on Bing")

def search_google(query):
    if query!= '':
        url = f"https://google.com/search?q={query}"
        webbrowser.get().open(url)
        speak(f"Googling your request")

def search_wikipedia(query):
    speak("Searching for " + query + " on wikipedia.")
    result = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia, " + result)

