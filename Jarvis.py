import pyjokes
import pyttsx3
import datetime
# import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
voicerate = 200
engine.setProperty('rate', voicerate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    speak("current time is")
    speak(datetime.datetime.now().strftime("%H:%M:%S"))


def date_():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)


def wishme():
    hrs = int(datetime.datetime.now().hour)
    if hrs < 12:
        speak("good morning ")
    elif 12 < hrs < 18:
        speak("good afternoon")
    elif hrs > 18:
        speak("good evening")


def getcommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            speak(query)
            print(f"User said: {query}\n")

        except:
            # print(e)
            print("Say that again please...")
            return "None"
        return query


def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    speak("Hello User how can i help u")

      # date_()
    while True:
        query = getcommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            wb.open("youtube.com/watch?v=50VNCymT-Cs")

        elif "google" in query:
            wb.open("google.com")

        elif "play music" in query:
            location = 'D:\\mobile backup\\Gym song'
            songs = os.listdir(location)
            print(songs,end="\n")
            x= random.randint(0, (len(songs)-1))
            print(x)
            os.startfile(os.path.join(location, songs[x]))

        elif "time" in query:
            time()

        elif 'chrome' in query:
            speak("what should i search")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"
            chromepath = getcommand().lower()
            print(chromepath)
            wb.get(path).open_new_tab(chromepath+'.com')

        elif "visual code" in query:
            path = "C:\\Users\\Anshu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'email to anshu' in query:
            try:
                speak("What should I say?")
                content = getcommand()
                to = "anshuyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend Anshu. I am not able to send this email")

        elif 'logout' in query:
            os.system("shutdown - 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'stop' in query:
            speak("thank u")
            break

        elif "remember that" in query:
            speak("what should i remember")
            notes = getcommand()
            speak(f"you said that {notes}")
            remember = open("text.txt", "w")
            remember.write(notes)
            remember.close()

        elif "remember anything" in query:
            remember = open("text.txt", "r")
            speak(f"you once said that remember jarvis {remember.read()}")
            print(remember.read())
            remember.close()

        elif "joke" in query:
            jokes()

        else:
            exit()
