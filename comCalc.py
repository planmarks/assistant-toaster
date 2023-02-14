import re
import speech_recognition as sr
import pyttsx3
import os
import time


def speak(audio, rate = 120):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(audio)
    engine.runAndWait()

import re

def calculate(query):
    query = re.sub('[^0-9^ +^-^*^/^(^)]', '', query)
    if not query:
        speak("No expression provided. Please provide an expression to calculate.")
        return None

    try:
        result = eval(query)
    except ZeroDivisionError:
        speak("Cannot divide by zero. Please try again with a different expression.")
        return None
    except SyntaxError:
        speak("Invalid syntax. Please try again with a valid expression.")
        return None
    except:
        speak("Error evaluating expression. Please try again with a different expression.")
        return None

    speak(f"The result of {query} is {result}")
    return result


