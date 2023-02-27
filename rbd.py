#initial settings for selenium
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



#assigning webdriver to a variable for further use
driver = webdriver.Chrome(options=options)
for i in range(20):
    driver.get('https://eticket.co/')
    driver.switch_to.new_window('tab')
