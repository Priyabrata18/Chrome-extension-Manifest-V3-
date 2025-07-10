import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# to recognize your voice or sound or audio
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    # sometimes microphones doesnot work or might some trouble
    try:
        with sr.Microphone() as source:
            print('listening...')
            # create a variable to listen to the source
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'baby' in command:
                command = command.replace('baby', '')
                print(command)

    except:
        pass
    return command


def run_baby():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'please tell me' in command:
        person = command.replace('please tell me', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a Headache')
    elif 'are you single' in command:
        talk('I am in a relationship with WiFi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_baby()