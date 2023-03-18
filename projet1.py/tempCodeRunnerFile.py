import speech_recognition as sr
import pyttsx3

# initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# set up text-to-speech engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # set voice to default

# set up language for speech recognition
with sr.Microphone() as source:
    print("Set up your language")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
try:
    lang_code = r.recognize_google(audio, language='en-US')
    print("Language code set to: " + lang_code)
except sr.UnknownValueError:
    print("Sorry, I didn't understand what language you spoke.")
    lang_code = 'en-US'

# main loop for listening to speech and outputting text
while True:
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # recognize speech
        text = r.recognize_google(audio, language=lang_code)

        # output recognized speech
        print(text)

        # Narator

        #engine.say(text)
        #engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    
    #except sr.RequestError as e:
       #print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))
