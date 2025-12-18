import pyttsx3
import time
import speech_recognition as sr
from tasks import greeting, weather, volume, schedule, app_caller
import openpyxl
import requests

data_parser = ''

def speak(text):
    rate = 100
    print(text)
    engine = pyttsx3.init()
    voice = engine.getProperty("voices")
    engine.setProperty("voices", voice[1].id)
    engine.setProperty("rate",rate+50)
    engine.say(text)
    engine.runAndWait()

def excel():
    wb = openpyxl.load_workbook('word_book.xlsx')
    wuse = wb['Users']
    wrep = wb['Replies']

    global hello_list1
    global hello_list2
    urow1 = wuse['1']
    urow2 = wuse['2']
    hello_list1 = [urow1[x] for x in range(len(urow1))]
    hello_list2 = [urow2[x] for x in range(len(urow2))]

    global reply_list1
    global reply_list2
    rrow1 = wrep['1']
    rrow2 = wrep['2']
    reply_list1 = [rrow1[x] for x in range(len(rrow1))]
    reply_list2 = [rrow2[x] for x in range(len(rrow2))]


def start(r, source):
    print('Awaiting keyword activation....')
    r.listen_in_background(source, callbacks)
    time.sleep(1000000)

def recog_main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_wit(audio_data=audio, key='FC7G3QKQBOPYOMAUQCK7HYAQN27SQKD3').lower()
        greeting.greeting(data, speak, hello_list1, hello_list2)
        
        if 'weather' in data:
            speak('Fetching weather information...')
            speak(weather.weather())
        if 'schedule' in data:
            speak('Adding a new schedule entry...')
            schedule.add_entry()
        if 'volume' in data:
            speak('Adjusting volume...')
            volume.volume()
        if 'search' in data:
            speak('searching...')
            print(search_engine(data))
                

        print(f' "{data}" recognized') 
        data_parser = data
    except sr.UnknownValueError:
            print('Calex did not understand your request')
    except sr.RequestError as e:
            print('Sorry could not fulfill your request')
   
def callbacks(recognizer, audio):
    try:
        sdata = recognizer.recognize_wit(audio_data=audio, key='FC7G3QKQBOPYOMAUQCK7HYAQN27SQKD3')
        speak('Yes sir')
        recog_main()
        time.sleep(30)
    except sr.UnknownValueError:
        print("Sorry, I didn't quite catch that, repeat please")
    

def search_engine(text):
    url = "https://www.googleapis.com/customsearch/v1"
    api = open("API_KEY").read()
    search = open("SEARCH_ID").read()
    query = text
    param = {
        'q':query,
        'key':api,
        'cx':search
    }
    return requests.get(url, params=param)