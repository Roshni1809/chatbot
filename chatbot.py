import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

if __name__ == "__main__":
    speak("Hello I am ChatBot")