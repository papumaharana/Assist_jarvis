import pyttsx3
import os
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib, ssl
import openai_codes as oc
import image_gen
import mtranslate as mt

engine = pyttsx3.init()

## Creating a function for speak:
def speak(audio):
    # audio = mt.translate(audio, to_language='hi', from_language='en-in')
    engine.say(audio)
    engine.runAndWait()


def command():
    content = ' '
    while content == ' ':
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            print('Recognising.....')
            content = r.recognize_google(audio, language='en-in')
            # print(content)
            ## for translate to english:
            content = mt.translate(content, to_language='en-in')
            print("You said : " + content)
        except Exception as e:
            print("Could not understand...")
            speak("Could not understand")
    return content

## Creating main function:
def main_process():
    jarvis_chat = []
    while True:
        request = command().lower()
        if 'hello' in request:
            speak('welcome sir! how can i help you?')
        # elif 'jarvis' in request:
        #     speak('yes sir!')
            
        ## Playing music:
        elif 'play music' in request:
            speak('playing music')
            song = random.randint(1, 3)
            if song == 1:
                webbrowser.open('https://www.youtube.com/watch?v=9XXGCb4Eev8')
            elif song == 2:
                webbrowser.open('https://www.youtube.com/watch?v=QjcZfh7Dwfc')
            else:
                webbrowser.open('https://www.youtube.com/watch?v=Qw6cyRwJ9fI')
        
        ## Opening websites:
        elif "open youtube" in request:
            speak('opening youtube')
            webbrowser.open('www.youtube.com')
        elif "open facebook" in request:
            speak('opening facebook')
            webbrowser.open('www.facebook.com')
        elif "open linkedin" in request:
            speak('opening linkedin')
            webbrowser.open('www.linkedin.com')

        ## Time and date:
        elif "what's the time" in request:
            time = datetime.datetime.now().strftime('%H:%M')
            speak(f'current time is {str(time)}')
        elif "what's the date" in request:
            date = datetime.datetime.now().strftime('%d:%m')
            speak(f'current date is {str(date)}')
        
        ## Todo lists:
        elif 'make note' in request:
            note = request.replace('make note', '')
            note = note.strip()
            if note != '':
                speak('adding note'+ note)
                with open('todo.txt', 'a') as file:
                    file.write(note +'\n')
        elif "what's the list" in request:
            with open('todo.txt', 'r') as file:
                speak('note that i have : '+ file.read())
        elif "show the list" in request:
            with open('todo.txt', 'r') as file:
                note = file.read()
            notification.notify(
                title = 'Note book',
                message = note
            )
        
        ## Opening window applications:
        elif "open" in request:
            query = request.replace('open', '')
            pyautogui.press('super')
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press('enter')
        
        ## Taking screenshots:
        elif 'take a screenshot' in request:
            date = datetime.datetime.now()
            # im1 = pyautogui.screenshot()
            scrn_name = f"screenshot_{date.strftime('%H.%M.%S__%d.%m.%y')}.jpg"
            im2 = pyautogui.screenshot(scrn_name)
            print('done.')
            speak('done')
        
        ## Search on wikipedia:
        elif "wikipedia" in request:
            request = request.replace('jarvis', '')
            request = request.replace('search wikipedia', '')
            print(request)
            result = wikipedia.summary(request, sentences=2)
            print(result)
            speak(result)
        
        ## Search on google:
        elif "search google" in request:
            request = request.replace('jarvis', '')
            request = request.replace('search google', '')
            print(request)
            webbrowser.open('https://www.google.com/search?q='+request)

        ## Message on whatsapp:
        elif "send whatsapp" in request:
            hr = int(datetime.datetime.now().strftime('%H'))
            mn = int(datetime.datetime.now().strftime('%M'))
            pwk.sendwhatmsg('+918658259266', 'Hii, how are u?', hr, mn+2, 10)
            
        ## Send Email:
        # elif 'send email' in request:
        #     pwk.send_mail(email_sender='mpapu177@gmail.com', password=user_config.gmail_app_pass, subject='hello', message='how are you', email_receiver='papum143@gmail.com')
        #     print('Email sent.')
        #     speak('Email sent')
        # or
        elif 'send email' in request:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("mpapu177@gmail.com", user_config.gmail_app_pass)
            message = '''
            This is text area.

            thank you
            '''
            s.sendmail("mpapu177@gmail.com", "papum143@gmail.com", message)
            s.quit()
            print('Email sent.')
            speak('Email sent')

        ## generate image:
        elif 'generate image' in request:
            request = request.replace('jarvis', '')
            request = request.replace('generate image', '')
            image_gen.generate_img(request)

        ## Boss name:
        elif 'who is your boss' in request:
            request = request.replace('jarvis', '')
            speak('Mr Papu maharana')

        ## Turn off jarvis:
        elif 'turn off' in request:
            request = request.replace('jarvis', '')
            speak('turning off')
            break

        ##chat with chatgpt:
        elif 'clear chat' in request:
            jarvis_chat = []
            speak('chat cleared')

        else:
            request = request.replace('jarvis', '')
            # print(request)
            jarvis_chat.append({'role':'user', 'content':request})
            result = oc.send_requests(jarvis_chat)
            jarvis_chat.append({'role':'assistant', 'content':result})
            print(result)
            speak(result)


entry = True
while entry:
    request = command().lower()
    if 'jarvis' in request:
        speak('yes sir!')
        entry = False
        main_process()

