import datetime
import random
import time

def greeting(data, speak, hello_list1, hello_list2):

    if data in hello_list1 or data in hello_list2:
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak('Good morning sir')
        elif hour >= 12 and hour < 18:
            speak('Good Afternoon sir')
        else:
            speak('Good Evening sir')
            time.sleep(5)
    else: 
        pass

    if 'time' in data:
        stime = datetime.datetime.now().strftime('%H%M')
        speak(f'The time is {stime}')
        time.sleep(5)
    elif 'What day is it' in data:
        days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
        cday = datetime.datetime.now().weekday()
        speak(f"It's {days[cday]}")
    else:
        pass