import platform
import subprocess
import pyautogui

class Browser:

    def __init__(self, browser):
        self.browser = browser
        self.process = None
        self.system = platform.system()
        # self.firefox_pid = None ?

    # Browser
    def open(self):
        self.process = subprocess.Popen([self.browser])

    def close(self):
        if self.system == "Linux":
            # способ закрытия для Linux
            subprocess.run(["kill", str(self.firefox_pid)])

        elif self.system == "Windows":
            # способ закрытия для Windows
            pass

        elif self.system == "Darwin":
            # способ закрытия для macOS
            pass

    #page
    # def search(self, search_address):
    #     pyautogui.hotkey("ctrl", "l")
    #     pyautogui.write(search_address)
    #     pyautogui.press("enter")