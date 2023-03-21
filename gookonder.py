"""Project requirements
*opens Chrome
*opens a set amount of tabs and
then organizes those tabs and
put some in groups names labels
and colors the groups
"""

# initial settings for selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# waiting for elements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# Rich library for pretty printing
from rich.prompt import Prompt
from rich.console import Console


# entering commands on the browswer window
import pyautogui
import sys
import os
import time


console = Console()


def request_number_of_tabs():

    quantity_of_tabs = Prompt.ask("Please enter the number of tabs to open")
    return int(quantity_of_tabs)


def request_sites_to_open(quantity_of_tabs):
    

    sites_to_open = []
    for tab in range(quantity_of_tabs):
        site_to_open = Prompt.ask(
            "Please provide the site that you would like to visit")
        sites_to_open.append(site_to_open)

    return sites_to_open

#opens
def open_browser(sites_to_open):
   
    options = Options()
    options.page_load_strategy = 'normal'
    # locators
    # keeping the browser open
    options.add_experimental_option("detach", True)

    # assigning webdriver to a variable for further use
    driver = webdriver.Chrome(options=options)

    for site in sites_to_open:

        if len(sites_to_open) == 1:
            driver.get(site)
            continue

            console.print(driver.current_url, style='white on blue')
        else:
            driver.get(site)
            original_window=driver.current_window_handle
            driver.switch_to.new_window('tab')
    #close the last tab from the loop
    driver.close()
    

def save_bookmarks():  
    pyautogui.hotkey('ctrl', 'shift', 'b')
    pyautogui.hotkey('ctrl', 'shift', 'd') 
    time.sleep(10)   
    pyautogui.write('computrabajo')
    pyautogui.hotkey('enter')
    time.sleep
    pyautogui.click(x=170,y=154)
    
def group_bookmarks():
    pass
"""
     pyautogui.click(x=174, y=81)
        pyautogui.click(x=1205, y=312)
        pyautogui.click(x=1348, y=112)
        pyautogui.keyDown('control')
        pyautogui.keyDown('shift')
        pyautogui.press('b')
"""


"""
"Define a description of your web page:
<meta name = "description" content = Free Web tutorials for HTML and CSS >
"""

def track_mouse():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)

    except KeyboardInterrupt:
        console.print('\n', style='white on blue')

def clear_screen():
    os.sys('clear')

many_tabs = request_number_of_tabs()
sites = request_sites_to_open(many_tabs)
browsers_tabs = open_browser(sites)
saved_bookmars = save_bookmarks()
mouse= track_mouse()
screen=clear_screen()