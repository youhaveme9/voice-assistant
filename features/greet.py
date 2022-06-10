import pyttsx3
from datetime import datetime
import utils.Speak as Speak

def greet():
        # Time
    time_hour = datetime.now().hour
    if (time_hour >= 0 or time_hour <= 12):
        Speak.speak("Good Morning! How may I help you?")

    elif (time_hour > 12 or time_hour <= 5):
        Speak.speak("Good Afternoon! How may I help you?")

    else:
        Speak.speak("Good Evening! How may I help you?")

