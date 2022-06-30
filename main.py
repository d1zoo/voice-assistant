import pyautogui
import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
from datetime import datetime
import wikipedia
import os
import winshell
from googletrans import Translator

wikipedia.set_lang("ru")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)






def weather():

    api = 'abc8186c9595903cbbfc032158b6b5df'
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = command
    complete_url = url + 'q=' + city + '&lang=ru' + '&appid=' + api
    response = requests.get(complete_url)

    if response.status_code == 200:

        data = response.json()

        main = data['main']

        temperature = main['temp'] - 273
        humidity = main['humidity']

        weather_report = data['weather']
        wind_report = data['wind']

        print(f"{city:-^35}")
        talk(f"Температура равна: {temperature} градусам")
        talk(f"Влажность равна: {humidity} процентов")
        talk(f"Описание погоды: {weather_report[0]['description']}")
        talk(f"Скорость ветра: {wind_report['speed']} метров в секунду")
    else:
        print("Error in the HTTP request")



def location():
    person = command.replace("где находится", '')
    search = command
    webbrowser.open("https://www.google.com/maps/place/" + search)
    talk("Открываю ")


def search_yt():
    person = command.replace('на youtube', '')
    search = command
    webbrowser.open("http://www.youtube.com/results?search_query=" + search)
    talk("Открываю " + person)

def search_google():
    person = command.replace('найди', '')
    search = command
    webbrowser.open("https://www.google.com/search?q=" + search)
    talk("Ищу " + person)


def trans():
    langinput=input('На какой язык вы бы хотели перевести:')
    translator = Translator()
    translate_text = translator.translate(str(command), dest=langinput)
    talk(translate_text.text)


def empty_rb():
    winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)



def date():
    year = int(datetime.now().year)
    month = int(datetime.now().month)
    date = int(datetime.now().day)
    talk("Сегодня ")
    talk(date)
    talk(month)
    talk(year)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    print(text)


def wishme():
    hour = datetime.now().hour
    if hour >= 6 and hour<12:
        talk("Доброе утро!")
        date()


    elif hour >=12 and hour<18:
        talk("Добрый день")
        date()


    elif hour >= 18 and hour<24:
        talk("Добрый вечер")
        date()


    else:
        talk("Доброй ночи")
        date()


    talk("Здравствуйте, я шавля. Чем я могу помочь?")


def take_command():

    r = sr.Recognizer()
    m = sr.Microphone(device_index=1)
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Слушаю...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Распознаю...")
        command = r.recognize_google(audio, language='ru-RU')
        print(f"Вы сказали: {command}\n")

    except Exception as e:
        print("Повторите пожалуйста...")
        return "Ничего"
    return command


def screenshot():
    img = pyautogui.screenshot()
    img.save(r'C:\Users\User\Desktop\voice\Media\screen.png')



if __name__ == "__main__":
    count=0
    wishme()

while True:
    command = take_command().lower()
    print(command)

    if 'поставь' in command:
       song = command.replace('поставь', '')
       talk('ставлю ' + song)
       pywhatkit.playonyt(song)


    elif 'времени' in command or 'час' in command:
        time = datetime.now().strftime('%H:%M:%S')
        talk('Текущее время ' + time)


    elif 'в википедии' in command:
        person = command.replace('в википедии', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


    elif 'свидание' in command:
        talk('Извините, но у меня болит голова')


    elif 'приложение' in command:
        os.startfile(r'C:\Users\User\Desktop\voice\main.py')
        talk('Открываю приложение')



    elif 'instagram' in command:
        webbrowser.open_new_tab('https://www.instagram.com/')
        talk('Открываю instagram')


    elif 'google' in command:
        webbrowser.open_new_tab('https://google.com/')
        talk('Открываю google')

    elif 'найди' in command:
        command = command.replace('найди',  '')
        search_google()

    elif 'на youtube' in command or 'ютуби' in command:
        command = command.replace('на youtube', '')
        search_yt()


    elif 'netflix' in command:
        webbrowser.open_new_tab('https://www.netflix.com/')
        talk('Открываю netflix')


    elif 'перезагрузи' in command:
        os.system('shutdown /r /t 1')


    elif 'выключи' in command:
        os.system('shutdown /s /t 1')


    elif 'выйди' in command:
        os.system('shutdown -l')

    elif 'скриншот' in command:
        screenshot()
        talk('Скриншот сделан')

    elif 'где находится' in command:
        command = command.replace('где находится', ' ')
        location()

    elif 'погода' in command:
        command = command.replace('погода ', '')
        weather()

    elif 'очисти' in command:
        empty_rb()
        talk("Корзина очищена")

    elif 'discord' in command:
        os.startfile(r'C:\Users\User\Desktop\Discord.lnk')
        talk('Открываю discord')

    elif 'кушать' in command:
        webbrowser.open_new_tab('https://glovoapp.com/kg/ru/bishkek/restorany_1/')

    elif 'переведи' in command:
        command = command.replace('переведи ', '')
        trans()

    elif 'кто' in command:
        talk('')


    elif 'пока' in command or 'до свидание' in command:
        quit()





    else:
        talk('Извините, не могли бы вы повторить?')

