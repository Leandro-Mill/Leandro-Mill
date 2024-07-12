#Simple AutoClicker that can be improved by most likey adding a hot key that can start and stop it, or a GUI
import time
import pyautogui
delay = 1*60
close_time = time.time()+delay
while True:
    pyautogui.click
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click()
    if time.time()>close_time:
        break
