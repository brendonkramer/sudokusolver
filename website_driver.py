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

    def start(self):
        self._driver.get('https://nine.websudoku.com/?')
        time.sleep(1)
        self._driver.maximize_window()

    def save_screen(self):
        self._driver.get_screenshot_as_file(file_name)

    def get_size_and_loc(self):
        size = self._driver.find_element(By.ID, 'puzzle_grid').size
        loc = self._driver.find_element(By.ID, 'puzzle_grid').location
        return [size,loc]

    def set_value(self, x, y, value):
        element = "//table[@id=\'puzzle_grid\']/tbody/tr"
        if y == 0:
            element += "/"
        else:
            element += "[" + str(y+1) + "]/"
        if x == 0:
            element += "td/"
        else:
            element += "td[" + str(x+1) + "]/"
        element += "input"
        web_element = self._driver.find_element(By.XPATH, element)
        web_element.send_keys(str(value))

    def submit(self):
        submit_btn = self._driver.find_element(By.NAME, "submit")
        submit_btn.click()
        time.sleep(5)
        self.set_difficulty()

    def set_difficulty(self):
        print("Input Difficulty:\n"
              "1 - Easy\n"
              "2 - Medium\n"
              "3 - Hard\n"
              "4 - Evil\n")
        difficulty = input()
        if difficulty == '1':
            self._driver.get('https://nine.websudoku.com/?')
        else:
            self._driver.get('https://nine.websudoku.com/?level=' + difficulty)
