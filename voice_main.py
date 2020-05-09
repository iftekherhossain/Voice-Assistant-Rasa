import requests
import speech_recognition as sr 
#from playsound import playsound as ps
from gtts import gTTS
import subprocess

bot_message = ""
message = ""

while bot_message !='Bye':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything :")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("You said :{}".format(message))
        except:
            print("Sorry couldnot recognize your voice")
    if(len(message)==0):
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message":message})

    print("Bot says,",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")
    #print('yos')
    myobj = gTTS(text=bot_message,lang='en')
    myobj.save("bot_output.mp3")
    #print('saved')
    subprocess.call(['vlc',"bot_output.mp3",'--play-and-exit'])