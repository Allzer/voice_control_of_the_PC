from src.recognizer.command_router import CommandRouter
from src.controllers.browser import Browser
from src.controllers.youtube import YouTube
from src.recognizer.recognizer import Recognizer
import speech_recognition as sr
from config import Config

def main():
    recognizer = Recognizer()
    command_router = CommandRouter(
        controllers=[
            Browser(browser=Config.firefox_path)
        ]
    )
    
    with sr.Microphone() as mic:
        recognizer.calibrate(mic=mic)
        
        while True:
            command = recognizer.recognize(mic=mic)
            
            print(command)
            
            if command is None:
                continue
            
            if command == "компьютер стоп" or command == "computer stop":
                break
            
            if not command_router.dispatch(command=command):
                print("Неизвестная комманда")
            
if __name__ == "__main__":
    print("Работа началась")
    main()