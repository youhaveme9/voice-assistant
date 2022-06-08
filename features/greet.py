import pyttsx3
from datetime import datetime


class Greet:

    def greet(self):

        engine = pyttsx3.init()

        # Volume
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 1.0)

        # Voice
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        # Time
        time_hour = datetime.now().hour
        if (time_hour >= 0 or time_hour <= 12):
            # Greet

            engine.say('Good Morning ! How may I help you?')
            engine.runAndWait()
            engine.stop()
        elif (time_hour > 12 or time_hour <= 5):
            # Greet

            engine.say('Good Afternoon ! How may I help you?')
            engine.runAndWait()
            engine.stop()
        else:
            # Greet

            engine.say('Good Evening ! How may I help you?')
            engine.runAndWait()
            engine.stop()


person = Greet()
person.greet()
