import speech_recognition as sr
import pyttsx3
import random
import datetime
import webbrowser
import vlc
import time
import tkinter

def speak(ss):
    engine = pyttsx3.init()
    engine.say(str(ss))
    engine.runAndWait()

ti = datetime.datetime.now()
hour = ti.hour
print(ti)
song = vlc.MediaPlayer("songs/song.mp3")
if hour in range(0,4) or hour in range(22 , 24):
    greet = "sir ... it is time to sleep"
elif hour in range(5,12):
    greet = "Good morning  sir"
elif hour in range(11 , 15):
    greet = "Good Afternoon sir"
elif hour in range(15 , 20):
    greet = "good evening"
else:
    greet = " good night "


speak(greet)


print("Speak Anything :")
while 1>0 :
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try :
            text = r.recognize_google(audio)
            print(text)
        except :
            print("I couldn't hear You ")
        while text != "" :
            if "hello" in text :
                speak("hello domy")
                text = ""
            elif "stop" in text and 'music' in text:
                text = ""
                song.stop()
            elif "your name" in text or "who are you" in text :
                speak("iam DOMO .... Your virtual assistant")
                text = ""
            elif "love you" in text or "love me" in text :
                speak("i love you so much ..... Domy")
                text = ""
            elif "joke" in text :
                jokes = ["What’s the difference between England and a tea bag? ... The tea bag stays in the cup longer" , "Why did the chicken commit suicide? To get to the other side" , "I went to the doctor the other day and said: ‘Have you got anything for wind?’ So he gave me a kite"]
                joke  = random.choice(jokes)
                speak(joke)
                text = ""
            elif "who is me"  and "who is me" in text or "who am I" in text or "my name" in text  :
                speak("You are Domy ..  my creator ")
                text = ""
            elif  text == "hey domo" or text == "domo" :
                speak("yes  sir")
                text = ""
            elif "how are you" in text :
                speak("iam fine .. thanks domy")
                text = ""
            elif "hey" in text :
                speak("hey .. domy")
                text = ""
            elif "help" in text :
                speak("sure ...  how can i help you")
                text = ""
            elif "play audio" in text or "play" in text and "music" in text :
                speak("ok")
                song.play()
                text = ""
            else :
                url = "https://www.google.com/search?q=" + text    
                webbrowser.open(url)
                sentences = ['that is what i found' ,' here you are ' , 'ok .. i think it will be helpful']
                sentence = random.choice(sentences) 
                
                speak(sentence)
                text = ""
