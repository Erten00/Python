import speech_recognition as sr
import pyttsx3

# initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # set voice to default

lang_code = 'en-US'

# listen to speech and output text
with sr.Microphone() as source:
    print("\nSay something! \n")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    # recognize speech and output recognized speech
    response = r.recognize_google(audio, language=lang_code, show_all=True)
    text = response['alternative'][0]['transcript']
    is_final = response['final']

    if is_final:
        print(text)

        # speak the recognized speech
        engine.say(text)
        # engine.runAndWait()

except sr.UnknownValueError:
    print("Sorry, I didn't understand what you said.")
except sr.RequestError as e:
    print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))