import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)



def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good After noon!')

    else:
        speak('Good night! sir')  

    speak('I am Jarvis. Tell me how i may help you')

def takeCommand():
    #it takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)

        print("say that again please...")
        return "none"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

         #logic on executing task based on query
        if 'wikipedia' in query:
             speak('searching wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")     

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")    

        else 'open music' in query:
            music_dir = 'E:\\redmi 2\\sd card\\august 2019\\audios'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
