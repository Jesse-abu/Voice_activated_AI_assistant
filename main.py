"""This programme was made by Jesse"""

#Libraries.............................................
import speech_recognition as sr
from tasks import schedule, weather, volume
from Func import start, excel, search_engine, data_parser
import requests
from chatterbot import ChatBot


chatbot = ChatBot('cally')

call = input('> ')

print(chatbot.generate_response(call))

#Variables.............................................
r = sr.Recognizer()
source = sr.Microphone()


#Requests..............................................
#res = [item['link'] for item in search_engine('police').json()['items']]

#Main program..........................................

'''excel()

start(r, source)
    
print(f'last command: {data_parser}')
while 1:
    if 'exit' in data_parser:
        print('Exiting the program...')
        break'''
    
    

