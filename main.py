#module pyttsx3 it provides a engine to convert text to voice
#here 0 is used for david voice this is based on particular numbers have particular voices
#def function to convert text to speech
#takecommand is used to take a users command
#we have take speechrecognition to as sr to avoid lengthy process
#microphone is used to take a command from user
#listening is used to know that our jarvis is listening our words
#pause threashold is used to avoid the ending of jarvis when we have stop in giving instruction to jarvis
#try is used to avoid errors
#recognize is to know our jarvis is recognizing our worlds or not
#wish is used to ask jarvis that is good morning and other something
#datetime module is used to indicate time
#hour is a variable
#query is defined to used to store the input of user
#" double qutes are used to define any directory
#cv2 module is used to display camera
#0 is type to used its internal camera
#list dir is used to convert music files into a particular list

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=3, phrase_time_limit=12)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<17:
        speak("good afternoon")
    elif hour>=17 and hour<20:
        speak("good evening")
    else:
        speak("good night")
    speak("I am jarvis sir, please tell me what can i help you")

#to send mail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()
    



if __name__ == "__main__":
    wish()
    # takecommand()
    # speak("hello sir")
    # speak("this is advance jarvis")

    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            apath = "C:\\Windows\\notepad.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open paint" in query:
            ppath = "C:\\WINDOWS\\system32\\mspaint.exe"
            os.startfile(ppath)

        elif "open adobe reader" in query:
            rpath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(rpath)

        elif "play music" in query:
            music_dir = "D:\From E - Drive\Surekha Chaudhari Songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play random music" in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "play mp3 music" in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = requests.get("https://api.ipify.org").text
            speak(f" Your IP address is: {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif "open youtube" in query:
            speak("Sir, what should I search on youtube")
            b = takecommand().lower()
            webbrowser.open(f"{b}")

        elif "play songs on youtube" in query:
            speak("Sir, which song I play on youtube")
            c = takecommand().lower()
            kit.playonyt(f"{c}")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("Sir, what should I search on google")
            a = takecommand().lower()
            webbrowser.open(f"{a}")

        elif "open scholarship" in query:
            webbrowser.open("https://mahadbtmahait.gov.in/Login/Login")

        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif "send message" in query:
            kit.sendwhatmsg('+919130671544', 'Hi',15,33)

        elif "open web" in query:
            webbrowser.open("https://web.whatsapp.com/")
            

        elif "email to rahul" in query:
            try:
                speak("what should i say")
                content = takecommand().lower()
                to = "rahuldalavi21122000@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to rahul")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to rahul")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("Sir, do you have any other work")
