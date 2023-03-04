#initial settings for selenium
import sys
import pyautogui
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton



options = Options()
options.page_load_strategy = 'normal'

#locators
#keeping the browser open
options.add_experimental_option("detach", True)
for i in range(2000):
    pyautogui.click(x=175, y=119)


try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    console.print('\n', style='white on blue')
