def save_bookmarks(sites):
    for site in sites:
        pyautogui.click(x=1239, y=123)
        pyautogui.click(x=1205, y=312)
        pyautogui.click(x=1348, y=112)
        pyautogui.keyDown('control')
        pyautogui.keyDown('shift')
        pyautogui.press('b')