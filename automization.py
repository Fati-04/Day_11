import time
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.moveTo(1909, 62, duration=0.8)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(1803, 183, duration=0.8)
pyautogui.click()
pyautogui.typewrite("https://pyautogui.readthedocs.io/en/latest/mouse.html", interval=0.02)
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
pyautogui.hotkey('win', 'r')
time.sleep(0.5)
pyautogui.typewrite('notepad', interval=0.05)
pyautogui.press('enter')
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.1)