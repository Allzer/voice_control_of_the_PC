import datetime
import os
import speech_recognition


class Recognizer:
    sr = speech_recognition.Recognizer()
        
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)

        while True:
            try:
                audio = sr.listen(source=mic)
                command = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                print(command)
                if command == "компьютер стоп":
                    break
            except Exception as e:
                print(e)