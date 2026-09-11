import pyautogui
import subprocess

subprocess.Popen(["firefox"])
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://google.com")
pyautogui.press("enter")
