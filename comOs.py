import speech_recognition as sr
import pyttsx3
import os
import time
import winshell
import dirCleanUp
import pyautogui
import numpy as np
import cv2



def speak(audio, rate = 120):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(audio)
    engine.runAndWait()

def record_speech():
    print("Recording your speech. Say stop when you're done.")
    speak("Recording your speech. Say stop when you're done.")
    filename = "Speech_" + str(int(time.time())) + ".txt"
    filepath = os.path.join(os.path.expanduser("~/Desktop"), filename)
    with open(filepath, "w") as file:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            while True:
                audio = r.listen(source)
                try:
                    speech = r.recognize_google(audio, language='en-in')
                except sr.UnknownValueError:
                    print("Sorry, I could not understand your speech.")
                except sr.RequestError as e:
                    print("Could not request results from speech recognition service; {0}".format(e))
                else:
                    file.write(speech + "\n")
                    print(speech)
                    if "stop" in speech.lower():
                        break

def empty_recycle_bin():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
    speak("Recycle bin emptied")

def directory_cleanup():
    speak("Provide directory path")
    dir_location = input()
    if os.path.exists(dir_location):
        dirCleanUp.clear_dir(dir_location)
        speak('Directory is organized')

