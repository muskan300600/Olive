import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''Add doc string'''
    hour = int (datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("A very good morning. Have a great day")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon. May your afternoon be light, blessed, enlightened, productive and happy.")

    else:
        speak("Wishing you a very wonderful evening. Look at the sunset and smile")

    speak("Hi! I'm your Mate . How may I assist you?")

def takeCommand():
    '''Add doc string'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print("User said:", query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query



if __name__ == '__main__':
  wishMe()
  takeCommand()
