import openai
import speech_recognition as sr
import pyttsx3
from keys import API_KEY


openai.api_key = API_KEY

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

prompt = ""
user_name = 'Sandeep'
bot_name = 'Assistant'
convo=""

while True:
    with mic as source:
        print('\n Listening... \n')
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)
    print('Completed Listening \n')

    try:
        user_input = r.recognize_google(audio)
    except:
        engine.say("Failed Recognizing Input")
        continue

    output = user_name + ":" + user_input + "\n" + bot_name + ":"
    convo = convo + output

# openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=convo,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response['choices'][0]['text'].replace("\n","")
    response_str = response_str.split(
        user_name + ":",1)[0].split(bot_name + ":",1)[0]
    
    convo += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()