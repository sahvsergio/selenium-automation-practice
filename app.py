
# library to beautify project.
from rich.console import Console
from rich.prompt import Prompt

# initial settings for selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


import sys
import os
import pyautogui

options = Options()
options.page_load_strategy = 'normal'

# locators
# keeping the browser open
options.add_experimental_option("detach", True)


# assigning webdriver to a variable for further use
driver = webdriver.Chrome(options=options)
# request_product

console = Console()
product = Prompt.ask('what\'s the product to search')

# request urls


def request_urls():
    """requests 4 different urls to be used by the program at a later time

    Returns:
        str:return 
    """
    urls = []
    for url in range(4):
        url = Prompt.ask('Please provide new url')
        urls.append(url)
        print(urls)
    return urls


# opening the websites

def open_markets():
    """uses the urls from

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    urls = request_urls()
    original_window_handle = driver.current_window_handle

    for url in urls:
        driver.get(url)
        driver.switch_to.new_window('tab')
        pyautogui.click(x=1222, y=79)


def search_product(product):

    action = driver.send_keys(Keys.ALT+str(range(1, 4)))


urls = request_urls
markets = open_markets()


"""

searches for a product in each market
gets the cheapest
from the cheapest, get the highest rated
sends it to a csv
sends file through email
use selenium, python_
"""
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    console.print('\n', style='white on blue')

# def :


"""

if 'amazon' in driver.current_url:
    
    search = driver.find_element(By.XPATH, '// *[@id="twotabsearchtextbox"]')

    search_field_input = search.send_keys('Necronomicon'+Keys.ENTER)
    dropdown= driver.find_element(By.XPATH, '// *[@id="search"]/span')
    ActionChains(driver)
    
    
    
    # xpath for the product part  //*[@id="search"]/div[1]/div[1]/div/span[1]
    
elif 'panamericana' in driver.current_url:
    popup = driver.find_element(By.ID, "wpn-popup-backdrop")
    ActionChains(driver).move_to_element_with_offset(popup, 8, 0).perform()
    
    
    search = driver.find_element(By.XPATH, '//*[@id="ftBoxf29a3e53497248579223c5e0920af827"]')

    search_field_input = search.send_keys('Necronomicon'+Keys.ENTER)
elif 'buscalibre0 in driver.current_url:
     search_field_input = search.send_keys('Necronomicon'+Keys.ENTER)

    

def search_product(product,):
    product=product
   
    if 'amazon' in driver.current_url:
        search = driver.find_element(
            By.XPATH, '// *[@id="twotabsearchtextbox"]')
        search_field_input = search.send_keys('Necronomicon'+Keys.ENTER)
        dropdown = driver.find_element(By.XPATH, '// *[@id="search"]/span')
        ActionChains(driver)
    elif 'panamericana' in driver.current_url:
        pass
        

        
        
    
"""
"""
//*[@id="twotabsearchtextbox"]

buscalibre xpath
/html/body/header/section[2]/section/div/div[2]/div/div/form/div[1]/input

panamericans
//*[@id="ftBoxf29a3e53497248579223c5e0920af827"]
"""
os.system('clear')
