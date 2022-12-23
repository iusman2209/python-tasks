import pyautogui

import time
time.sleep(5)

count=5
while count > -100036 :
    pyautogui.typewrite("your phone has been hacked - timeleft: " +str(count))
    pyautogui.press("enter")
    count=count-1

