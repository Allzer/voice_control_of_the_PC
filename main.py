import time

from src.controllers.browser import Browser
from config import Config

browser_handler = Browser(Config.firefox_path) 
browser_handler.open()
browser_handler.search(search_address="как испечь пирог")
time.sleep(5)
browser_handler.click_on_first_sites()
time.sleep(5)
browser_handler.close()