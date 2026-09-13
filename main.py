import time

from src.controllers.browser import Browser
from config import Config

browser_handler = Browser(Config.firefox_path) 
browser_handler.open()
browser_handler.minimize()
browser_handler.new_tab()
browser_handler.normalize()
time.sleep(3)
browser_handler.close()