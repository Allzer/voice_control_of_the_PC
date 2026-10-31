import pyautogui

class Video:

    def next_video(self):
        pyautogui.hotkey("shift", "n")

    def previous_video(self):
        pyautogui.hotkey("shift", "p")

    def pause(self):
        pyautogui.hotkey("k")

    def rewind_10_seconds_forward(self):
        pyautogui.hotkey("l")

    def rewind_10_seconds(self):
        pyautogui.hotkey("j")
        
    def rewind_5_seconds_forward(self):
        pyautogui.hotkey("right")
        
    def rewind_5_seconds(self):
        pyautogui.hotkey("left")
        
    def turn_up_volume(self):
        pyautogui.hotkey("up")
    
    def turn_down_volume(self):
        pyautogui.hotkey("down")
        
    def click_mute(self):
        pyautogui.hotkey("m")

    def click_full_size(self):
        pyautogui.hotkey("fN")
    #base
    def can_handel(self, command: str):
        return command.startswith("видео")
    
    
    #parser
    def execute(self, command: str):
        if "следующее" in command:
            self.next_video()
        if "предыдущее" in command:
            self.previous_video()
        if all(word in command for word in ("10", "секунд", "назад")):
            self.rewind_10_seconds()
        if all(word in command for word in ("10", "секунд", "вперёд")):
            self.rewind_10_seconds_forward()
        if all(word in command for word in ("5", "секунд", "назад")):
            self.rewind_5_seconds()
        if all(word in command for word in ("5", "секунд", "вперёд")):
            self.rewind_5_seconds_forward()
        if "пауза" in command:
            self.pause()
        if "мьют" in command:
            self.click_mute()
        if "mute" in command:
            self.click_mute()
        if "громче" in command:
            self.turn_up_volume()
        if "тише" in command:
            self.turn_down_volume()
        if all(word in command for word in ("на", "весь", "экран")):
            self.click_full_size()