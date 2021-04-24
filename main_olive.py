import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

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
        speak("Good Afternoon.")

    else:
        speak("Wishing you a very wonderful evening.")

    speak("Hi! I'm Olive . How may I assist you?")


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


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your_password')
    server.sendmail('email@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open kaggle' in query:
            webbrowser.open("kaggle.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\mini9\\Desktop\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open VisualStudio' in query:
            codepath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codepath)

        elif 'email to mini' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, I was unable to send the Email. Try again please")

        elif 'switch off' in query:
            speak("Glad I helped you, Bye")
            exit()
