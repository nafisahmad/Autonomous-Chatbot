
from imdb.Movie import Movie
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import requests
import pywhatkit
import time
from youtube_search import YoutubeSearch
import playsound
import wolframalpha
import imdb
import pyjokes

wakeWords = ["hey friday", "ok friday", "you there friday", "wake up friday", "hi Friday" "hai friday", "friday are you up", "you up friday"]
shutdownWords = ["shutdown", "power off", "back to sleep", "go back to sleep", "go to sleep", "exit", "quit"]
wikiWords = ["wikipedia", "according to wikipedia", "search wikipedia for", "who is", "tell me about"]
searchGoogle = ["search google"," find in google", "on google"]
findLocation = ["locate", "find location", "find this location", "locate a place", "find a location", "locate this place", "find this place"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weatherCheck = [ "get weather", "what is the weather", "check weather", "weather information", "wetaher details", "how is the weather"]
yesWords = ["yeah","sure", "ok","yes","go on","fine", "yup", "go for it"]
noWords = ["no","no need","naco", "nope", "nop", "not now"]
musicWords = ["sing a song", "play music", "music friday", "i am feeling groovy"]
thanks = ["thanks", "thank you", "thankyou Friday"]
Shop = ["shopping", "by", "buy", "buy something", "amazon", "buy products", "lets do some shopping"]
Movies = ["IMDB", "movie", "rating", "plot", "movie name", "movie information"]

edge_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('edge', None,webbrowser.BackgroundBrowser(edge_path))

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

print(voices)
for voice in voices: 
   # to get the info. about various voices in our PC  
    #  print("Voice:") 
    #  print("ID: %s" %voice.id) 
    #  print("Name: %s" %voice.name) 
    #  print("Age: %s" %voice.age) 
    #  print("Gender: %s" %voice.gender) 
    #  print("Languages Known: %s" %voice.languages)   
 
    engine.setProperty("voice", voices[0].id)

# volume = engine.getProperty("volume")
# engine.setProperty("volume", 2)
# engine.setProperty("rate",180)

def Speak(audio):

    # '''
    # Parameters
    # ----------
    # audio : TYPE
    #     DESCRIPTION.
    #     Enables FRIDAY to speak
    # Returns
    # -------
    # None.

    # '''
    
    print("Friday: " + audio)
    engine.say(audio)
    engine.runAndWait()
        
def WishMe():
    # '''
    # Enables FRIDAY to wish according to hour of the day

    # Returns
    # -------
    # None.
    # '''

    Speak("Initializing all systems")
    playsound.playsound("C:\\Users\\Nafis Ahmad\\Desktop\\Friday\\Ironman-Friday-Virtual-Assistant\\HUD Activation Sound Effect.mp3")
    playsound.playsound("C:\\Users\\Nafis Ahmad\\Desktop\\Friday\\Ironman-Friday-Virtual-Assistant\\FridayBoot.mp3")
    Speak("All systems loaded")
    Speak("I have indeed been uploaded sir. We're on-line and ready.")
    
    currentDay = datetime.datetime.now().strftime("%a, %b %d, %Y")
    Speak("Today is " + str(currentDay))
    
    strTime=datetime.datetime.now().strftime("%I:%M %p")
    Speak(f"It is {strTime}")
    
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        Speak("Good Morning boss! ")
        
    elif hour>=12 and hour<18:
        Speak("Good Afternoon boss!")
        
    elif hour>=18 and hour<22:
        Speak("Good evening boss")
        
    else:
        Speak("Good evening boss, or, should i say good night!")
        
    #Speak("Friday. Version 5.0 . At your service sir")    

def TakeCommand():
    '''
    Enables FRIDAY to take commands from the user(specifically
    takes microphone input and returns string output)
    Returns
    -------
    String.
    '''
    r=sr.Recognizer()
    r.energy_threshold=275
    with sr.Microphone() as source:
        print("Listening Boss...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        query = r.recognize_google(audio,language="en-US")
        print(f"Boss: {query}\n")
        
    except Exception:
        print("Sorry I didn't catch that boss")
        return ""
    
    return query

def GetWeather(city = "bangalore"):
    
    try:
        wquery = "q=" + city
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+wquery+'&APPID=ff8585ce61d82f73e1f43fb01a601385&units=metric')
        result = res.json()
        tempStr = "The temperature in " + city + " as of now is " + str(result["main"]["temp"]) + " degree celsius"
        tempStr2 = "But it may vary between " + str(result["main"]["temp_min"]) + " degree celsius" + " and " + str(result["main"]["temp_max"]) + " degree celsius"
        weatherStr = "Weather : " + str(result["weather"][0]["description"])
        windSpeedStr = "The wind speed is " + str(result["wind"]["speed"]) + " metre per second"
        humidityStr = "The humidity is " + str(result["main"]["humidity"]) 
        
        Speak(tempStr)
        
        if not result["main"]["temp_min"] == result["main"]["temp_max"]:
            Speak(tempStr2)
        
        Speak(weatherStr)
        Speak(windSpeedStr)
        Speak(humidityStr)
     
    except:
        Speak("Sorry boss but this location seems to be off the map")


if __name__ == "__main__":
    WishMe()
    while True:
        query = TakeCommand().lower()
    
        #Logic for executing tasks based on query(command)    

        for phrase in wikiWords:
            if phrase in query:
                Speak("Hang on for a second sir...")
                try:
                    query=query.replace(phrase, "")
                    results=wikipedia.summary(query,sentences=2,auto_suggest=True,redirect=True)
                    Speak(results)
                except wikipedia.exceptions.PageError:
                    Speak("Sorry boss, got nothing on that in my database")

                    Speak("Would you like me to search the web boss?")
                    answer = TakeCommand().lower()

                    for phrase in yesWords:
                        if phrase in answer:

                            url = "https://google.com/search?q=" + query
                            webbrowser.get("edge").open_new_tab(url)
                            Speak("This is what i found boss")
                    
                    for phrase in noWords:
                        if phrase in answer:
                            Speak("Alright boss")    
                
        if "the time" in query:
            strTime=datetime.datetime.now().strftime("%I:%M:%S %p")
            Speak(f"It is {strTime} boss")        


        if "MusicWords" in query:
            strTime=datetime.datetime.now().strftime("%I:%M:%S %p")
            Speak(f"It is {strTime} boss")

        if "open youtube" in query: 
            Speak("Just a second sir")       
            webbrowser.get('edge').open_new_tab("youtube.com")
            Speak("And yup. There you go sir") 
            
        if "open google" in query:
            Speak("Well don't we all just love google? Just a second sir")
            webbrowser.get('edge').open_new_tab("google.com")
            Speak("Search away boss")
            
        if "python module" in query:
            Speak("These python modules remind me of my source code days")
            webbrowser.get("edge").open_new_tab("pypi.org")
            Speak("As always sir, a great pleasure watching you work.")
            
        for phrase in musicWords:
            if phrase in query:
                Speak("Do you have anything specific in mind or do you want me to surprise you?")
                wish = TakeCommand().lower()
                Speak('playing ' + wish)
                pywhatkit.playonyt(wish)
                
                if "surprise me" in wish:    
                    url = "https://ytroulette.com/?c=1&l=en"
                    webbrowser.get("edge").open_new_tab(url)
                    Speak("Alright boss")
                    break
                
                else:
                           
                    Speak("Sorry boss but i don't think i can really sing this one")
                    Speak("Would you like me to search the web boss?")
                    answer = TakeCommand().lower()
                    for phrase in yesWords:
                        if phrase in answer:
                            results = YoutubeSearch(wish , max_results=3).to_dict()
                            url = "http://www.youtube.com" + results[0]["url_suffix"]
                            webbrowser.get("edge").open_new_tab(url)
                            Speak("This is what i got boss")
                            break
                                                        
                Speak("Alright boss")
                                 
        if "command prompt" in query:
            cPromptPath='C:\\Windows\\System32\\cmd.exe'
            Speak("Accessing Commandline Prompt")
            os.startfile(cPromptPath)
            Speak("This never gets old boss.")

        if "ppt" in query:
            Speak("Opening p p t")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            Speak("Wish i could make Presentations like you boss")
                
        if "excel" in query:
            Speak("Opening Microsoft Excel")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
            Speak("Train me with microsoft excel boss, i will do these for you without charge")

        if "open word" in query:
            Speak("Opening Microsoft word")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            Speak("Are we writing an essay boss?")

        if "notepad" in query:
            Speak("Opening notepad")
            os.startfile("C:\\WINDOWS\\system32\\notepad.exe")
            Speak("this still saves time.")
        
        if "who are you" in query:
            Speak("I am Friday, Your virtual assistant.")
            Speak(("My source code is written in python."))
            Speak("Since i am in my initial stages of development, my capabilities as of now,  are quite limited.")
            Speak("But i will be glad to serve you in every way i can, within the limits of my capabilities boss.")
        
        if "you feeling?" in query:
            Speak("peachy boss.")


        if "joke" in query:
            Speak(pyjokes.get_joke())

        for phrase in thanks:
            if phrase in query:
                Speak("always a pleasure boss")


        for phrase in wakeWords:
            if phrase in query:
                Speak("Right here boss")
                
        for phrase in shutdownWords:
            if phrase in query:
                Speak("It's been a pleasure serving you boss.")
                Speak("Initializing shutdown sequence.")
                playsound.playsound("C:\\Users\\Nafis Ahmad\\Desktop\\Friday\\Ironman-Friday-Virtual-Assistant\\system shut down sound FX.mp3")
                Speak("All systems offline sir")
                exit()
                
        for phrase in searchGoogle:
            if phrase in query:
                Speak("What do you wanna search boss?")
                search = TakeCommand().lower()
                url = "https://google.com/search?q=" + search
                webbrowser.get("edge").open_new_tab(url)
                Speak("This is what i found boss")
                    
        for phrase in findLocation:
            if phrase in query:
                Speak("What do you want me to locate boss?")
                search = TakeCommand().lower()
                url = "https://google.nl/maps/place/" +search + "/&amp;"
                webbrowser.get("edge").open_new_tab(url)
                Speak("This is what i got sir")
                
        if "what  month" in query:
            currentTime = datetime.datetime.now()
            Speak("It is "+ months[currentTime.month - 1] + " boss")
            
            
        if "what year" in query:
            currentTime = datetime.datetime.now()
            Speak("It is " + str(currentTime.year) + " boss")
                        
                            
        if "what day" in query:
            currentDay = datetime.datetime.now().strftime("%a, %b %d, %Y")
            Speak("Today is " + str(currentDay) + " boss")                   
                        
        if "how is the weather" in query:
            GetWeather()    
        
        for phrase in weatherCheck:
            if phrase in query:
                Speak("What is the location boss?")
                search = TakeCommand().lower()
                Speak("This is what i got boss")
                GetWeather(search)    
                               
        if "search youtube" in query:
            Speak("What would you like to search for boss?")
            uwish = TakeCommand().lower()
            url = "https://www.youtube.com/results?search_query=" + uwish
            webbrowser.get("edge").open_new_tab(url)
            Speak("Hang on a second boss")
            Speak("And there you go")


        for phrase in Shop:
            if phrase in query:
                Speak("What would you like to search for boss?")
                uwish = TakeCommand().lower()
                url = "https://www.amazon.in/s?k=" + uwish
                webbrowser.get("edge").open_new_tab(url)
                Speak("Hang on a second boss")
                Speak("And there you go")