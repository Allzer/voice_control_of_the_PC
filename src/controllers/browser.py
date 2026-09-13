import subprocess
import time

import psutil
import win32con
import win32gui
import win32process
import pyautogui
from config import Config
from pywinauto import Desktop
import pyperclip
class Browser:

    def __init__(self, browser):
        self.browser = browser
        self.process = None
        self.system = Config.system
        self.pid = None
        self.hwnd = None

    def _get_firefox_windows(self):
        windows = set()
        def callback(hwnd, _):
            if not win32gui.IsWindowVisible(hwnd):
                return
            try:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                process = psutil.Process(pid)
                if process.name().lower() == "firefox.exe":
                    windows.add(hwnd)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        win32gui.EnumWindows(callback, None)
        return windows
 

    # Browser
    def open(self):
        if self.system == "Linux":
            self.process = subprocess.Popen([self.browser])
        elif self.system == "Windows":
            old_windows = self._get_firefox_windows()
            self.process = subprocess.Popen([self.browser])
            for _ in range(50):
                time.sleep(0.1)
                current_windows = self._get_firefox_windows()
                new_windows = current_windows - old_windows
                if new_windows:
                    self.hwnd = new_windows.pop()
                    return
            raise RuntimeError("Не удалось найти новое окно Firefox")


    def close(self):
        if self.system == "Linux":
            # способ закрытия для Linux
            subprocess.run(["kill", str(self.pid)])

        elif self.system == "Windows":
            # способ закрытия для Windows
            if self.hwnd is None:
                return

            if win32gui.IsWindow(self.hwnd):
                win32gui.PostMessage(
                    self.hwnd,
                    win32con.WM_CLOSE,
                    0,
                    0
                )

            self.hwnd = None
            self.process = None

        elif self.system == "Darwin":
            # способ закрытия для macOS
            pass
    
    def minimize(self):
        if self.hwnd is None:
            return
        if win32gui.IsWindow(self.hwnd):
            win32gui.ShowWindow(self.hwnd, win32con.SW_SHOWMINIMIZED)
            time.sleep(0.1)
            
    def normalize(self):
        if self.hwnd is None:
            return
        if not win32gui.IsWindow(self.hwnd):
            return
        
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOWMAXIMIZED)
        win32gui.SetForegroundWindow(self.hwnd)
        
    def new_tab(self):
        if self.hwnd is None:
            return
        pyautogui.hotkey('ctrl', 't')

    #page
    def search(self, search_address):
        pyperclip.copy(search_address)        
        pyautogui.hotkey("ctrl", "l")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
    
    def click_on_first_sites(self):
        firefox = Desktop(backend="uia").window(handle=self.hwnd)

        documents = firefox.descendants(control_type="Document")
        if not documents:
            return

        document = documents[0]

        links = document.descendants(control_type="Hyperlink")

        for link in links:
            rect = link.rectangle()

            if rect.top < 250:
                continue

            link.click_input()
            return