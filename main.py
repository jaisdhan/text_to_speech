import pyttsx3

engine = pyttsx3.init()

with open('OCI_AI.txt', 'r') as f:
    text = f.read()

voices = engine.getProperty("voices")

engine.setProperty("rate", 200)
engine.setProperty("voice", voices[1].id)

#engine.say(text)
engine.save_to_file(text, 'OCI_AI.mp3')
engine.runAndWait()


