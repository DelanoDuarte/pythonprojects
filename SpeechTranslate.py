import speech_recognition as sr
from textblob import TextBlob


class Main:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Time to Talk !!!')
        audio = r.listen(source)

        try:
            textTalked = r.recognize_google(audio)

            textToTranslate = TextBlob(textTalked)

            print('You said:', textTalked)

            textToTranslate.translate(textToTranslate, to="fr")
            print(textTalked)
        except sr.UnknownValueError:
            print('Google speech could no recognize the audio !')
