import speech_recognition 
import webbrowser
import pyttsx3
import musicLib
import requests
from openai import OpenAI


recognizer = speech_recognition.Recognizer()
newsapi ="MY API KEY"
engine = pyttsx3.init()

def speck(text):
    engine.say(text)
    engine.runAndWait()

def AIprocess(command):
     client = OpenAI(api_key="MY API KEY")

     completion = client.chat.completions.create(
          model="gpt-4o-mini",
          store=True,
          messages=[
               {"role": "user", "content": command}
          ]
        )
     return completion.choices[0].message.content  

def processCommand(c):
    if "open google" in c.lower():
          webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
          webbrowser.open("https://www.facebook.com/")
    elif "open instagram" in c.lower():
          webbrowser.open("https://www.instagram.com/")
    elif "open youtube" in c.lower():
          webbrowser.open("https://www.youtube.com/") 
    elif c.lower().startswith("play"):
         song = c.lower().split(" ")[1]
         link = musicLib.music[song]
         webbrowser.open(link)


    elif "news" in c.lower():
         r = requests.get("GET https://newsapi.org/v2/everything?q=Apple&from=2025-06-24&sortBy=popularity&apiKey=dff07e0f166a4258b9f5d05c0fd15567")
         if r.status_code == 200:
                data = r.json()
                articles = data.get("articles",[])
                for article in article:
                     speck(article['title'])

    else:
        output =  AIprocess(command)
        speck(output)
if __name__=="__main__":
    speck("Hey Jerry")

    while True:
        recognizer = speech_recognition.Recognizer()
        print("Recgonize....")
        try:
            with speech_recognition.Microphone() as source:
                print("Listening ..... ")
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=2)
                command = recognizer.recognize_google(audio)
                word = recognizer.recognize_google(audio)
                if(word.lower() == "jerry"):
                     speck("yah")

                with speech_recognition.Microphone() as source:
                     print("Jerry Active ....")
                     audio = recognizer.listen(source)
                     command = recognizer.recognize_google(audio, language="en-IN")

                     
                     processCommand(command)

        except speech_recognition.UnknownValueError:
            print("Could not understand the audio") 
        except speech_recognition.RequestError as e:
                print("Error; {0}".format(e))
