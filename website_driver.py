#######################################################################################################################
# File: website_driver.py
#
#######################################################################################################################

# imports
import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config_file import file_name

class Driver():

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._first_cell = self._driver.find_elements(By.ID, 'f00')

    def start(self):
        self._driver.get('https://nine.websudoku.com/?')
        time.sleep(1)
        self._driver.maximize_window()
        self.save_screen()

    def save_screen(self):
        self._driver.get_screenshot_as_file(file_name)

    def enter(self, number):
        pass
