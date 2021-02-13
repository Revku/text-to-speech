import pyttsx3
tts = pyttsx3.init()

text = input(str("Insert text in english: "))

tts.say(text)
tts.runAndWait()