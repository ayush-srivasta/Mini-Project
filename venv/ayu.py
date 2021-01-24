import speech_recognition as sp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import wikipedia
import time
from playsound import playsound
from gtts import gTTS as gt
import threading
from datetime import datetime
import datetime
import subprocess
import os
import cv2

 #it takes input from micrphone and convert it in text form and return
def listen():
    with sp.Microphone() as micro:
        try:
            global pr
            pr=sp.Recognizer()
            pr.energy_threshold=700
            pr.adjust_for_ambient_noise(micro,0.5)
            audio=pr.listen(micro)
            # print("Yaha tak to jaa raha hai")
            text=pr.recognize_google(audio,language="en-in")
            return text
        except Exception:
            msg="Sorry i did not get it repaet it again"
            print(msg)
            audio = gt(msg, lang='en', slow=False)
            audio.save("start_sound.mp3")
            playsound('start_sound.mp3')
            os.remove("start_sound.mp3")
            listen()
# This function will decide which function to call on the basis of the user command


def functionality():
   while True:
        open_msg=wish()+"What you want me to do"
        audio = gt(text=open_msg, lang='en', slow=False)
        audio.save("start_sound.mp3")
        playsound('start_sound.mp3')
        os.remove("start_sound.mp3")
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
        elif('browser' in fin_text):
            open_browser()
        elif(option=='Set' or option=='set'):
            reminder()
        elif 'calculator' in fin_text:
            calculator()
        elif 'Notepad' in fin_text:
            openNodepad()
        if to_repeat():
            continue
        else:
            speek="Program is terminating"
            audio = gt(text=speek, lang='en', slow=False)
            audio.save("last_voice.mp3")
            playsound('last_voice.mp3')
            break




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


# this function will set a reminder
def reminder():
    actual_time=datetime.now()
    ab=actual_time
    print(actual_time)
    actual_time=str(actual_time)
    year=int(actual_time[0:4])
    month=int(actual_time[5:7])
    day=int(actual_time[8:10])
    # print(year)
    # print(month)
    # print(day)
    hour=int(input("Enter the hour "))
    minute=int(input("Enter the minute"))
    alarm_time=datetime(year,month,day,hour,minute,0)
    diffrence=(alarm_time-ab)
    diffrence=diffrence.total_seconds()
    diffrence=int(diffrence)
    # print(diffrence)

    temp = "ok your reminder is set and i will inform you after"+str(diffrence)+"seconds"

    audio = gt(text=temp, lang='en', slow=False)
    audio.save("summ.mp3")
    playsound('summ.mp3')
    os.remove('summ.mp3')
    timer=threading.Timer(diffrence,alarm_sound)
    timer.start()


# this function contains the alarm sound which we are using in the reminder function
def alarm_sound():
    playsound("C:\\Users\\Ayush\\PycharmProjects\\mini_project\\venv\\Lib\\site-packages\\alarm.mp3",True)



# this function will open calculator
def calculator():
    subprocess.Popen("C:\\Windows\\System32\\calc.exe")


# this fucntion will open notepad
def openNodepad():
    subprocess.Popen("C:\\Windows\\System32\\notepad.exe")


# this function will decide to terminate or to repeat the function
def to_repeat():
    temp="You want to continue"
    audio = gt(text=temp, lang='en', slow=False)
    audio.save("to_repeat_sound.mp3")
    playsound('to_repeat_sound.mp3')
    os.remove("to_repeat_sound.mp3")
    text=listen()
    print(text)
    if text=="yes" or text=="Yes":
        return True
    else:
        return False
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        w = "Good Morning"
    elif 12 <= hour < 18:
        w = "Good Afternoon"
    else:
        w = "Good Evening"
    return w

# main function
if __name__ == "__main__":
    functionality()





