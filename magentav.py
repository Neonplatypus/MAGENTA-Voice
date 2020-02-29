import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<=11:
        speak("Good Morning!")
    elif hour>=13 and hour<17:
        speak("Good Afternoon!")
    elif hour>=19 and hour>=4:
        speak("Good Night")     
    else:
        speak("Please Once again Check your Code in time Division")
    speak("Hello, its your MAGENTA how may i help you")
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..........")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print("Sorry i can not hear you please say that again........")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com','pass')
    server.sendmail('email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
  wishMe()
  while True:

    query = takeCommand().lower()


    if 'wikipedia' in query:
        speak('searching Wikipedia.....')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    

    elif 'play music' in query:
        music_dir = 'E:\\'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'open visual studio' in query:
        codepath = "C:\\Users\\rizas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif 'open virtualbox' in query:
        codepath = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
        os.startfile(codepath)

    elif 'email to ' in query:
        try:
            speak("what should i write?")
            content = takeCommand()
            to = "email@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("I am sorry i m not be able to send this email at this moment")





    



