from __future__ import print_function
import openai
import pyttsx3
import threading
import tkinter as tk
import keys
import webbrowser
from tkinter.constants import DISABLED
from Mail import Mail
from Maps import Maps
from Time import Time
from Bin import Recycle
from Audio import Audio
from Openapp import Open
from Search import Search
from Date import Today_date
from Wolfram import Wolfram
from Notepad import Notepad
from Image_Generation import Generate_Img
from Wallpaper import Wallpaper

openai.api_key = keys.API_KEY
voice_id=0
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[voice_id].id)

def Toggle_voice():
    global voice_id
    voice_id=1-voice_id
    engine.setProperty('voice', voices[voice_id].id)

def Toggle():
    global b
    b=True
    Input()

def on_enter_pressed(event):
    global b
    b=True
    Input()

prompt = ""
user_name = 'User'
bot_name = 'Assistant'
convo = ""
b=False

BG_GRAY = "#ABB289"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"



def Input():
    global b
    global convo
    if(b):
        user_input = input_text.get("1.0", tk.END).strip()
        convo += user_name + ":" + " " + user_input + "\n" + bot_name + ":"
        input_text.delete("1.0", tk.END)
        b=False
        #Taking Input From Text Box
    
    else:
        user_input = Audio()  # 6 sec
        convo += user_name + ":" + user_input + "\n" + bot_name + ":"

    keywords = ["calculate", "compute", "math", "solve"]  # Wolfram

    if any(keyword in user_input.lower() for keyword in keywords):
        response_str = Wolfram(user_input)

    elif "open" in user_input.lower():
        response_str = Open(user_input.lower())

    elif "date" in user_input.lower():
        response_str = Today_date()
    
    elif "time" in user_input.lower():
        response_str = Time()
    
    elif "search" in user_input.lower():
        response_str = Search(user_input)
    
    elif "change background" in user_input.lower() or "change wallpaper" in user_input.lower():
        response_str = Wallpaper()  

    elif "empty recycle bin" in user_input.lower():
        response_str = Recycle()
    
    elif "where is" in user_input.lower() or "find the location of" in user_input.lower():
        response_str = Maps(user_input)

    elif "generate an image " in user_input.lower():
        n=1
        url = Generate_Img(user_input,n)
        response_str = "Generated Image is opening in Browser"
        webbrowser.open(url)

    elif "send an email" in user_input.lower():
        engine.say("To whom would you like to send")
        engine.runAndWait()
        mail = Audio()
        engine.say("What would you like to Send ?")
        engine.runAndWait()
        content = Audio()
        response_str = Mail(mail,content)
    
    elif "make a note" in user_input.lower():
        engine.say("What would you like me to write down?")
        engine.runAndWait()
        Note_prompt = Audio()
        res = Notepad(Note_prompt)
        response_str = "Noted!" 
    
    elif "change your voice" in user_input.lower():
        engine.stop()
        Toggle_voice()
        response_str = "Sure! Your wish is my Command"

    elif "calendar" in user_input.lower():
        response_str = Calendar()

    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=convo,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_str = response['choices'][0]['text'].replace("\n", "")
        response_str = response_str.split(
            user_name + ":", 1)[0].split(bot_name + ":", 1)[0]

    convo += response_str + "\n"
    conservation_text.delete("1.0", tk.END)
    conservation_text.insert(tk.END, convo)

    engine.say(response_str)
    engine.runAndWait()


window = tk.Tk()
window.title("Smart Assistant")
window.configure(width=500, height=570, bg=BG_COLOR)

# head label # 
# make it random  
# Gigglesnort! Hilaritidings! Jocularity ahoy! Laughterwaves! Mirthful salutations! Witty-waves! Humorific hello!
# Chortle-infused greetings! Guffaw-filled delights! Jolly jests to you!
head_label = tk.Label(window, bg=BG_COLOR, fg=TEXT_COLOR, text="Salutations, fellow Earthlings!", font=FONT_BOLD, pady=10)
head_label.place(relwidth=1)

# tiny divider
line = tk.Label(window, width=450, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)

# text widget
conservation_text = tk.Text(window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
conservation_text.place(relheight=0.745, relwidth=1, rely=0.08)
conservation_text.configure(cursor="arrow")

# scroll bar
# scrollbar = tk.Scrollbar(conservation_text)
# scrollbar.place(relheight=1, relx=0.974)
# scrollbar.configure(command=conservation_text.yview)

# bottom label
bottom_label = tk.Label(window, bg=BG_GRAY, height=80)
bottom_label.place(relwidth=1, rely=0.825)

input_text = tk.Text(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
input_text.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
input_text.focus()
input_text.bind("<Return>", on_enter_pressed)

text_button = tk.Button(bottom_label, text="Text", font=FONT_BOLD, bg=BG_GRAY, width=20,
                        command=lambda: threading.Thread(target=Toggle).start())
text_button.place(relx=0.77, rely=0.008, relheight=0.03, relwidth=0.22)

audio_button = tk.Button(bottom_label, text="Audio", font=FONT_BOLD, bg=BG_GRAY, width=20,
                         command=lambda: threading.Thread(target=Input).start())
audio_button.place(relx=0.77, rely=0.04, relheight=0.03, relwidth=0.22)

window.mainloop()