from datetime import datetime
import time
from playsound import playsound

schedule = []



def add_entry():
    task = input("Task: ")
    description = input("Description: ")
    event = input("Event: ")

    schedule.append(
    {
    'date':f"{datetime.today()}",
    'task':task,
    'description':description,
    'event':event
})
    print(schedule)
    
