import speech_recognition as sr
# import Speak

def takecommand():
    # takes voice input from user and return output as string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # maximum pause time in voice
        audio = r.listen(source)
    try:
        print("Recognizing....")
        input=r.recognize_google(audio, language='en-in')
        print("You said:", input)
        # Speak.speak(input)
    except Exception as e:
        print("Can't recognize you! Please Speak again")
        # Speak.speak("Can't recognize you! Please Speak again")
        return "none"
    return input



