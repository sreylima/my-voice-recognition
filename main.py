import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import re
import random
import screen_brightness_control as sbc
import subprocess


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, timeout=30)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
        return command
    except:
        talk("Time out! Good Bye!")
        exit()


def run_alexa():
    command = take_command()
    if 'music' in command:
        path = 'C:\Program Files (x86)\Windows Media Player\wmplayer.exe'
        subprocess.call(path)
    elif 'play' in command:
        output = re.sub(r'.*?(?=play)', '', command, 1)
        print(output)
        song = output.replace('play', '')
        print(song)
        talk('play'+song)
        pywhatkit.playonyt(song)
    elif 'brightness' in command or 'bright' in command:
        if 'to' in command:
            brightness = re.sub(r'.*?(?=to)', '', command, 1)
            no_to = brightness.replace('to', '')
            if '%' in command or 'a hundred':
                no_to = no_to.replace('%' or 'a hundred', '')
                sbc.set_brightness(no_to)
                talk('Screen brightness has been set to' + no_to)
            else:
                sbc.set_brightness(no_to)
                talk('Screen brightness has been set to'+no_to)
        else:
            talk('Which level of brightness do you want to set?')
            command = take_command()
            brightness = re.sub(r'.*?(?=to)', '', command, 1)
            no_to = brightness.replace('to', '')
            if '%' in command or 'a hundred':
                no_to = no_to.replace('%' or 'a hundred', '')
                sbc.set_brightness(no_to)
                talk('Screen brightness has been set to' + no_to)
            else:
                sbc.set_brightness(no_to)
                talk('Screen brightness has been set to' + no_to)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is '+time)
    elif 'who' in command or 'what' in command or 'where' in command or 'how' in command:
        ask = command.replace('who' or 'what' or 'where' or 'how', '')
        info = wikipedia.summary(ask, 2)
        print(info)
        talk(info)
    elif 'search' in command:
        search = command.replace('search', '')
        howto = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('https://google.com/search?q=' + search)
        print(howto)
        talk('I got this for you on'+search)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'open' in command:
        filedir = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
        fileext = r".lnk"
        filename = command.replace('open', '')
        filename = filename.strip()
        files_path = [os.path.join(filedir, _) for _ in os.listdir(filedir) if _.endswith(fileext)]
        for path in files_path:
            filename = filename.capitalize()
            if filename in path:
                talk(filename + 'has been opened.')
                subprocess.call(path, shell=True)
                break
            else:
                if 'notepad' in command:
                    subprocess.call('notepad.exe')
                    break
                if 'calculator' in command:
                    subprocess.call('calc.exe')
                    break
                if 'calendar' in command:
                    subprocess.call("explorer shell:AppsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar", shell=True)
                    break
                if 'mail' in command:
                    subprocess.call("explorer shell:AppsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.mail", shell=True)
                    break
                if 'control' in command or 'control panel' in command:
                    subprocess.call('control.exe')
                    break
                if 'command' in command or 'cmd' in command or 'command prompt' in command or 'terminal' in command:
                    subprocess.call('explorer C:\Windows\system32\cmd.exe')
                    break
                if 'file explorer' in command or 'explorer' in command:
                    subprocess.call('explorer.exe')
                    break
    elif 'location' in command:
        location = command.replace('location', '')
        here = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('https://www.google.com/maps/place/'+location+'/&amp;')
        talk('Here is the location for '+location)
    elif 'girl friend' in command or 'boy friend friend' in command or 'relationship' in command:
        gfbf = ["Sorry, I have a boyfriend.", "No, we'd better be friend!"]
        talk(random.choice(gfbf))
    elif 'on a date' in command:
        ondate = ["Sure, When do you want to go?", "I'm free on Sunday.", "Let's go picnic! YAY!"]
        talk(random.choice(ondate))
    elif 'girl friend' in command or 'boy friend friend' in command:
        again = ["Sorry, I have a boyfriend.", "No, we'd better be friend!"]
        talk(random.choice(again))
    elif 'stop' in command or 'exit' in command or 'bye' in command:
        talk('Good bye. Have a nice day')
        exit()
    elif 'hi' in command or 'hey' in command or 'hello' in command:
        talk('Hi, My name is Alexa. I am your personal assistant. What can I help you?')
    else:
        again = ["Sorry, I didn't catch that.", "Sorry, I didn't catch that.", "I don't quite get what you said"]
        print(random.choice(again))


while True:
    run_alexa()

