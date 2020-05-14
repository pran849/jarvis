
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Aftrnoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Mam. Please tell me how can i help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-hi")
        print(f"user said:{query}\n")
    except Exception as e:
       # print(e)
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    #speak("pranjal is a good girl")
    wishMe()
    while True:
        query=takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
           # chromePath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'open quora' in query:
            webbrowser.open("quora.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif "play music" in query:
            music_dir='E:\\Desktop\\PRANJAL DOCUMENTS\\pranjal'
            songs=os.listdir(music_dir)
            print(songs,end="")
            os.startfile(os.path.join(music_dir,songs[5]))
        
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, The time is {strTime}")

        elif "open code" in query:
            codePath="C:\\Users\\new\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "quit" in query:
            exit()