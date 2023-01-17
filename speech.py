from gtts import gTTS
import os

text = "Hi there! Just bored so I made this. I can use google speech api to make better audio results but its paid so meh. Gotta do with what I have."

language = 'en'

tts = gTTS(text=text, lang=language, slow=False)

tts.save("output.mp3")