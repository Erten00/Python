import speech_recognition as sr
import pyttsx3

# initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# set up text-to-speech engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # set voice to default

# main loop for listening to speech and outputting text
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # recognize speech
        text = r.recognize_google(audio)

        # output recognized speech
        print("You said: " + text)

        # speak the recognized speech
        engine.say(text)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError as e:
        print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))