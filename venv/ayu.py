import speech_recognition as sp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import wikipedia
import time
from playsound import playsound
from gtts import gTTS as gt
import threading
from datetime import datetime


 #it takes input from micrphone and convert it in text form and return
def listen():
    with sp.Microphone() as micro:
        global pr
        pr=sp.Recognizer()
        pr.energy_threshold=700
        pr.adjust_for_ambient_noise(micro,0.5)
        audio=pr.listen(micro)
        text=pr.recognize_google(audio,language="en-in")
    return text
# This function will decide which function to call on the basis of the user command
def functionality():
    text=listen().split()
    fin_text=""
    print(text)
    option=text[0]
    for i in range(1,len(text)):
        fin_text+=text[i]
        fin_text+=" "
    print(fin_text)
    if(option=="Play" or option=="play"):
        play_audio(fin_text)
    elif(option=='Who' or option=='who' or option=='What' or option=='what'):
        wiki(fin_text)
    elif(option=="Open" or option=='open'):
        open_browser()
    elif(option=='Set' or option=='set'):
        reminder()
    elif(option=='Yes' or option=='yes'):
        functionality()
    elif(option=='No' or option=='no'):
        exit(0)





# This function will play the songs
def play_audio(text):
    temp="https://www.youtube.com/results?search_query="
    path=r"C:\Users\Ayush\PycharmProjects\mini_project\venv\Lib\site-packages\selenium\webdriver\common\chromedriver.exe"
    options=webdriver.ChromeOptions()
    options.add_argument("headless")
    exe=webdriver.Chrome(executable_path=path,chrome_options=options)
    temp+=text+"Lyrics"
    exe.get(temp)
    exe.find_element_by_id("img").click()
    print("Press 'S' to stop")
    a=input()
    if(a=='S' or a=='s'):
        exe.__exit__()

# This function will take the info from wikipidea and play using playaudio
def wiki(ab):
    temp=wikipedia.summary(ab)
    audio=gt(text=temp, lang='en', slow=False)
    audio.save("summ.mp3")
    playsound('summ.mp3')

#This is the funtion to open a browser
def open_browser():
    path = r"C:\Users\Ayush\PycharmProjects\mini_project\venv\Lib\site-packages\selenium\webdriver\common\chromedriver.exe"
    browser=webdriver.Chrome(path)
    browser.get("https://www.google.com/")
    browser.find_element_by_class_name("gLFyf gsfi").click()

def reminder():
    actual_time=datetime.now()
    print(actual_time)
    hour=int(input("Enter the hour "))
    minute=int(input("Enter the minute"))
    alarm_time=datetime(2020,12,4,hour,minute,0)
    diffrence=(alarm_time-actual_time)
    diffrence=diffrence.total_seconds()
    print(diffrence)
    temp = "ok your reminder is set and i will inform you"
    audio = gt(text=temp, lang='en', slow=False)
    audio.save("summ.mp3")
    playsound('summ.mp3')
    timer=threading.Timer(diffrence,alarm_sound)
    timer.start()

def alarm_sound():
    playsound("C:\\Users\\Ayush\\PycharmProjects\\mini_project\\venv\\Lib\\site-packages\\alarm.mp3",True)



functionality()
temp = "Want to quit or do something more"
audio = gt(text=temp, lang='en', slow=False)
audio.save("su.mp3")
playsound('su.mp3')


