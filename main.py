import time

from src.controllers.browser import Browser
from config import Config

browser_handler = Browser(Config.firefox_path) 
browser_handler.open()
time.sleep(3)
browser_handler.close()