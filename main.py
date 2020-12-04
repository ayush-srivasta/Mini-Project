from selenium import webdriver
import  speech_recognition as sp
from selenium.webdriver.chrome.options import Options
import wikipedia
from gtts import gTTS as gt
from playsound import playsound




with sp.Microphone() as micro:
    global pr
    pr=sp.Recognizer()
    pr.energy_threshold=600
    pr.adjust_for_ambient_noise(micro,0.5)
    pr.pause_threshold=0.5
    audio=pr.listen(micro)


text=pr.recognize_google(audio,language="en-in")
print(text)
final_text=text.split()
text=""
print(final_text)
# who is mark 
for i in range(1,len(final_text)):
    text+=final_text[i]
print(text)

ch_driver=r"C:\Users\Ayush\PycharmProjects\mini_project\venv\Lib\site-packages\selenium\webdriver\common\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("headless")
ab=webdriver.Chrome(executable_path=ch_driver,chrome_options=options)

print(final_text)
if final_text[0]=='What' or final_text[0]=='what' or final_text[0]=='who' or final_text[0]=='Who':
    print(wikipedia.summary(final_text[3:]))
    var=wikipedia.summary(final_text[3:])
    out=gt(text=var,lang='en',slow=False)

    out.save('naya.mp3')
    playsound("naya.mp3")
    #ab.get("naya.mp3")


else:
#this is for playing audio
  play="https://www.youtube.com/results?search_query="
  play+=text+"+lyrics"
  ab.get(play)
  print(play)

  ab.find_element_by_id("img").click()
  print("enter some value")
  a=input()
  if(a=="F" or  a=='f'):
    ab.quit()