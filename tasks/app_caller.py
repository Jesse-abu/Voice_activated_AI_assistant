import subprocess
import webbrowser
import threading

def call_app(text):
    if 'web' in text:
        webbrowser.open('https://www.google.com')
    elif 'app' in text:
        print('Which app would you like to open?')
        