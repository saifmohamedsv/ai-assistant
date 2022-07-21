import random
import subprocess
import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import webbrowser
import os
import datetime
import calendar
import wikipedia
import ctypes
import winshell
import pyjokes
import smtplib

warnings.filterwarnings('ignore')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 0.75)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def GreetByName(name):
    talk(f"Hello {name}, I'm EDITH, your Artificial Intelligence assistant")


def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)

    except sr.UnknownValueError:
        print("ISSUE: I didn't understand what you're saying")
        talk("Can you please raise your voice so I can hear you")

    except sr.RequestError as ex:
        talk("I think there is a request error from google speech recognition")
        print("ISSUE: I think there is a request error from google speech recognition" + ex)

    return data


def response(text):
    tts = gTTS(text=text, lang="en")
    audio = "E:\PycharmProjects\jarvis\Audio.mp3"
    tts.save(audio)
    print(text)
    # playsound.playsound(audio)
    talk(text)
    os.remove(audio)


def call(text):
    action_call = "sam"

    text = text.lower().split()

    if action_call in text:
        return True

    return False


def today_date():
    now = datetime.datetime.now()

    date_now = datetime.datetime.today()

    week_now = calendar.day_name[date_now.weekday()]

    month_now = now.month

    day_now = now.day

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    ordinals = ['1st', '2nd', '3rd', '4th', '5th', '6th',
                '7th', '8th', '9th', '10th', '11th', '12th',
                '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21th', '22th', '23th',
                '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31th',
                ]

    return f'Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}.'


def say_hello(text):
    greetings = ['hello', 'hi', 'hola', 'wassup', 'hey', 'hey there']

    responses = ["Hi, Boss"]

    for word in text.split():
        if word.lower() in greetings:
            return random.choice(responses) + "."

    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == 'who' and list_wiki[i + 1].lower() == 'is':
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, 'w') as f:
        f.write(text)

    subprocess.Popen(['notepad.exe', file_name])

# not working method
def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("xcyberghostx1@gmail.com", "weekweeks1A")
    server.sendmail("vectorps11@gmail.com", "horeyatm@gmail.com", 'a7a')
    talk("Fuck you")



while True:

    try:
        text = rec_audio()
        # text = "sam where is usa"
        speak = " "

        if call(text):
            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = " "
                if now.hour > 12:
                    meridiem = " p.m"
                    hour = now.hour - 12
                else:
                    meridiem = " a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It's is " + str(hour) + ":" + minute + meridiem + " ."

            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki

            elif "who are you" in text:
                speak = speak + """Hello, I'm EDITH, Saif Artificial Intelligence assistant, You can ask me "
                                anything and I'll try to help you, I can solve mathematical operations and 
                                open or close programs"""

            elif "your name" in text:
                speak = speak + "My name is EDITH, like the ironman assistant"

            elif "who am I" in text:
                speak = speak + "you must probably be a human, no face recognition we don't have a camera, hehehe"

            elif "how are you" in text:
                speak = speak + "I'm fine, Thanks"
                speak = speak + "\n How are you ?!"

            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that you're fine"

            elif "open" in text.lower():
                if "google" in text.lower() or "chrome" in text:
                    speak = speak + "Opening Google Chrome.."
                    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

                elif "code editor" in text.lower() or "web storm" in text:
                    speak = speak + "Opening Web Storm Chrome.."
                    os.startfile(r"C:\Program Files\JetBrains\WebStorm 2022.1.2\bin\webstorm64.exe")

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube.."
                    webbrowser.open_new(r"https://youtube.com")
                else:
                    speak = speak + "Application not found"

            elif "shutdown" in text.lower():
                speak = speak + "Shutting down the pc..."
                os.system("shutdown /s /t 2")

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open_new('https://www.google.com/search?q=' + "+".join(search))
                speak = speak + f"Searching {str(text.lower())} on Google"

            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open_new('https://www.google.com/search?q=' + "+".join(search))
                speak = speak + f"Searching {text.lower()} on Google"

            elif "change background" in text or "change wallpaper" in text:
                img = r'G:\wallpapers'
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = speak + "Background Changed Successfully"

            elif "play music" in text:
                talk("Here you go with music")
                music_dir = r'G:\Music'
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                randomSong = os.path.join(music_dir, d)

            elif "note" in text or "remember that" in text:
                talk("What you would like me to write ?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I've written that"

            elif "joke" in text or "jokes" in text:
                speak = speak + pyjokes.get_joke()

            elif "where is" in text:
                ind = text.lower().split().index('is')
                location = text.split()[ind + 1:]
                print(location)
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where" + str(location) + "is."
                webbrowser.open_new(url)
            response(speak)

    except:
        print('Retrying')
