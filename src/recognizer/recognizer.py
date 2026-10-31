import speech_recognition as sr

class Recognizer:
    def __init__(self):
        self.engine = sr.Recognizer()
    
    def calibrate(self, mic):
        self.engine.adjust_for_ambient_noise(
            source=mic
        )
        
    def recognize(self, mic):
        audio = self.engine.listen(source=mic)
        try:
            return self.engine.recognize_google(audio_data=audio, language='ru-RU').lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print("Ошибка распознования: ", e)
            return None