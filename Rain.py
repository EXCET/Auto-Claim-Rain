import pyautogui
import time

time.sleep(2)
print('Started Sniping Rains')
def snipe():
 button_pos = pyautogui.locateOnScreen('play.PNG')
 pyautogui.moveTo(button_pos)
 time.sleep(1)
 pyautogui.click()
 print("[+] Robux")
 snipe()

snipe()