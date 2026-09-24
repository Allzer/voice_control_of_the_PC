import pyautogui
import pyperclip

from config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By

PAUSE_BUTTON = 'video-stream html5-main-video'
COPU_LINK = 'ytp-menuitem'

class YouTube:

    def next_video():
        pyautogui.hotkey("shift", "n")
    
    def previous_video():
        pyautogui.hotkey("shift", "p")
    
    def pause():
        pyautogui.hotkey("k")
    
    def rewind_10_seconds_forward():
        pyautogui.hotkey("l")
        
    def rewind_10_seconds():
        pyautogui.hotkey("j")
    
    def mute():
        pyautogui.hotkey("m")