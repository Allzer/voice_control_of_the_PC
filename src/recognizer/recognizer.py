import datetime
import os
import speech_recognition

sr = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)

    while True:
        try:
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            print(query)

        except Exception as e:
            print(e)