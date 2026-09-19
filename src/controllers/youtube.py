import pyautogui
import pyperclip

from config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By

PAUSE_BUTTON = 'video-stream html5-main-video'
COPU_LINK = 'ytp-menuitem'

class YouTube:
    # def __init__(self):
    #     self.browser = webdriver.Firefox()
    #     self.video_link = None
        
    def next_video(self):
        pyautogui.hotkey("esc")
    
    def pause():
        pyautogui.leftClick()