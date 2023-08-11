import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib




engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
 engine.say(audio)
 engine.runAndWait()   

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
            speak("Good Morning Anurag")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Cybrom")

    else :
     speak("Good evening Anurag")

def takeCommand():
    #taking microphone inp from user and returning string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1          # seconds of non-speaking audio before a phrase is considered complete
         audio= r.listen(source)
         
    try:
        print("Recognizing..")   
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said, {query}\n")
        
    except Exception as e:
        #print(e)    
        print("Say that again please....")
        return None
    return query


if __name__ == "__main__":
    wishMe()
    speak("I'm Jerry. Your personalized assistant. What can I assist you with?")
    while True:
        query=takeCommand().lower()
    
    #logics for query.
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to results from wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get("chrome").open("youtube.com")

        elif 'open google' in query:
            webbrowser.get("chrome").open("google.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\Anurag\\Music\\Spotify Music.'
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            str = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {str}")
        elif 'open code' in query:
            os.startfile(['code'])
        
        def sendEmail(to,content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('youremail@gmail.com', 'your-password')
            server.sendmail('youremail@gmail.com', to, content)
            server.close()

elif 'email to anurag' in 'query':
       try:
            speak("What should I say?")
            content = takeCommand()
            to = "dubey.anurag0711@gmail.com"    
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
                    print(e)
                    speak("Sorry Anurag. Email can't be sent..")      