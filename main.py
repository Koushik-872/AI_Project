import newsapi
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import smtplib
import pywhatkit
import os
import time
import wolframalpha
import shutil
import random
import requests
from urllib.request import urlopen

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am wall-e Sir. Please tell me how may I help you")


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("Welcome Mr.", uname.center(columns))

    speak("How can i Help you, Sir")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('kaushiknaresh872@gmail.com', 'your')
    server.sendmail('kaushiknaresh872@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    clear=lambda :os.system('cls')

    clear()
    wishMe()
    username()
    api_key="e2d45e2288224271b3cc0f00aa136442"
    app_id ="589JJ8-A7KG327P7R"
    weather_key ="93c8fffbe759747de92b957de2e98143"
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")


        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "what's my name" in query:
            speak(assname)
            print(assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'what can you do' in query:
            ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
             I can open websites for you, launch application and more. See the list of commands-"""
            li_commands = {
                "1:open websites": "Example: 'open youtube.com",
                "2:time": "Example: 'what time it is?'",
                "3:date": "Example: 'what date it is?'",
                "4:launch applications": "Example: 'launch chrome'",
                "5:tell me": "Example: 'tell me about India'",
                "6:weather": "Example: 'what weather/temperature in Mumbai?'",
                "7:news": "Example: 'news for today'",
                'So ':"now how can i help you?"}

            print(ans)
            speak(ans)
            print(li_commands)
            speak(li_commands)



        elif "who made you" in query or "who created you" in query:
            speak("I have been created by koushik and gauri.")

        elif "rock paper scissor" in query:
            speak("Just a warning i am all time champion So")
            speak("choose among rock paper or scissor")
            voice_data = takeCommand()
            moves=["rock", "paper", "scissor"]
            cmove = random.choice(moves)
            pmove = voice_data
            speak("i chose " + cmove)
            speak("You chose " + pmove)

            if pmove == cmove:
                speak("you should not feel low that's why i am letting this draw ")
            elif pmove == "rock" and cmove == "scissor":
                speak("Sir u wins")
            elif pmove == "rock" and cmove == "paper":
                speak("walle wins")
            elif pmove == "paper" and cmove == "rock":
                speak("Sir u wins")
            elif pmove == "paper" and cmove == "scissor":
                speak("walle wins")
            elif pmove == "scissor" and cmove == "paper":
                speak("Sir u wins")
            elif pmove == "scissor" and cmove == "rock":
                speak("walle wins")

        elif "calculate" in query:
            client = wolframalpha.Client('api_id')
            query=str(takeCommand('Query:'))
            res=client.query(query)
            try:
                output = next(res.results).text
                print(output)
                speak(output)
            except StopIteration:
                print("No results")            

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to koushik and group.Gratfully they wanted me for they group project ")
        elif "who are you" in query:
            speak("I am your virtual assistant created by koushik and group")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop wall-e from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'news' in query:
            main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
            news=requests.get(main_url).json()
            #print(news)
            article=news["articles"]
            #print(article)

            news_article=[]
            for arti in article:
                news_article.append(arti['title'])
                #print(news_article)
            for i in range(5):
                mainline=(i+1,news_article[i])
                speak(mainline)

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('walle.txt.', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("walle.txt", "r")
            notes = file.read()
            print(notes)
            speak(notes)
            file.close()

        elif "weather" in query:
            baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
            speak(" City name ")
            print("City name : ")
            cityname = takeCommand()
            completeUrl = baseUrl + cityname + "&appid=" + weather_key
            response = requests.get(completeUrl)
            data= response.json()

            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            weather_info = f"The weather in {cityname} is {weather_description}. The temperature is {temperature} Kelvin, and the humidity is {humidity}%."

            speak(weather_info)
            print(weather_info)

        elif "where is" in query:
            query = query.replace("where is", "")

            
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            app_id ="589JJ8-A7KG327P7R"
            client = wolframalpha.Client("589JJ8-A7KG327P7R")
            res = client.query(query)

            try: 
                result = next(res.results).text
                print(result)
                speak(result)
            except StopIteration:
                print("No results")



        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            
        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "vscode://file/C:/xampp/htdocs/AI/main.py"
            os.startfile(codePath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")






