from gtts import gTTS

with open("OCI_AI.txt", "r", encoding="utf-8") as f:
    text = f.read()

#Convert text to speech
tts = gTTS(text, lang="en")

tts.save("OCI_AI.mp3")