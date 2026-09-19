import time

from src.controllers.browser import Browser
from src.controllers.youtube import YouTube
from config import Config

browser_handler = Browser(Config.firefox_path)
youtube_handler = YouTube

browser_handler.open()
browser_handler.search(search_address="youtube.com")
time.sleep(5)
youtube_handler.pause()
time.sleep(5)
browser_handler.close()