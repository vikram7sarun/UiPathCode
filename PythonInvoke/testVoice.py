from gtts import gTTS
import os

def texttospeech(input):
	language = 'en'
	speech = gTTS(text=input, lang=language, slow=False)
	speech.save("C:/Users/ADMIN/Documents/UiPath_AllCode/UiPathCode/PythonInvoke/output/voice.mp3")
	os.system("Start C:/Users/ADMIN/Documents/UiPath_AllCode/UiPathCode/PythonInvoke/output/voice.mp3")
	return True

texttospeech("Praveen you are Chutiya")