import subprocess
import time

import psutil
import win32con
import win32gui
import win32process

from config import Config

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

    #page
    # def search(self, search_address):
    #     pyautogui.hotkey("ctrl", "l")
    #     pyautogui.write(search_address)
    #     pyautogui.press("enter")