import time

from src.controllers.browser import Browser

browser_handler = Browser(browser="firefox") 

browser_handler.open()
time.sleep(3)
browser_handler.close()