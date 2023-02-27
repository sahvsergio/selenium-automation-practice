"""Project requirements
We can start on Basics like for example a bot that opens Chrome
opens a set amount of tabs and
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

# Rich library for pretty printing
from rich.prompt import Prompt
from rich.console import Console


# entering commands on the browswer window
import pyautogui
import sys


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
            console.print(driver.current_url, style='white on blue')
        
    
   



def save_bookmarks(sites):
    for site in sites:        
        pyautogui.click(x=1239, y=123)
        pyautogui.click(x=1205, y=312)
        pyautogui.click(x=1348, y=112)
        pyautogui.keyDown('control')
        pyautogui.keyDown('shift')
        pyautogui.press('b')
    
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)

    except KeyboardInterrupt:
        console.print('\n', style='white on blue')


many_tabs = request_number_of_tabs()
sites = request_sites_to_open(many_tabs)
browsers_tabs = open_browser(sites)
saved_bookmars = save_bookmarks(sites)
