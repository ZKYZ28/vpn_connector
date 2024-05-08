import os
import time
import pyautogui

EXECUTABLE_PATH = r"C:\BIGIP\f5fpclientW.exe"

USERNAME = "username"
PASSWORD = "password"

def open_executable(path):
    if os.path.exists(path):
        os.system(f"start {path}")
        time.sleep(0.8)
        pyautogui.click(x=820, y=531)
        time.sleep(1.5)
        pyautogui.click(x=1053, y=486)

        time.sleep(2)
        pyautogui.click(x=1086, y=430)
        pyautogui.typewrite(USERNAME)

        time.sleep(0.5)
        pyautogui.click(x=1047, y=490)
        pyautogui.typewrite(PASSWORD)

        pyautogui.click(x=1100, y=553)
    else:
        print("The specified executable does not exist.")

open_executable(EXECUTABLE_PATH)

