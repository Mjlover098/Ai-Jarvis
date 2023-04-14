import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour>12:
       speak("Good Mornning!")

    elif hour>=12 and hour>18:
       speak("Good Afternoon!")

    else:
        speak("Good Evening!")  

    speak ("Hello im jarvis how can help you sir ")
    
def takecommand():

    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threeshold= 1
        audio = r.listen(source)

    try:
        print("Recognizing")   
        qurey =r.recognize_google(audio,Language='en-in')
        print(f"User said{qurey}\n")
             
    except Exception as e:
        
        print("Say that again please")
        return"None"
    return qurey
    
def sendEmail(dp,content):
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login('youremail@gmail.com', 'your-password')
     server.sendmail('youremail@gmail.com', to, content)
     server.close()

     
     if __name__=="__main__" :
      wishme()
while True: 
     if 1:
      qurey= takecommand().lower()

  
     if  'wikipedia'in qurey:
       speak('Searching wikipedia...')
       qurey = qurey.replace("wikipedia","")
       results =wikipedia.summary(qurey,sentences=2)
       speak("According to Wikipedia")
       print(results)
       speak(results)                     
         
     elif 'open youtube' in qurey:
      webbrowser.open("youtube.com")

     elif 'open google'  in qurey:
        webbrowser.open("google.com")

     elif 'open instagram' in qurey :  
        webbrowser.open("instagram.com")
 

     elif 'the time' in qurey:
        strTime= datetime.datetime.now().starttime("%H:%M:%S")
        speak(f"Sir ,the time is(strTime)")
    
     elif 'email to Omkar' in qurey:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "omkaryourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Omi Sir. I am not able to send this email")    

     
               