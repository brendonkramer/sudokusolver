#######################################################################################################################
# File: main.py
#
#######################################################################################################################
#imports
import os
import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from image_processing import process_image_file

#constants
file_name = "puzzle.png"

def start():
    driver = webdriver.Chrome()
    driver.get('https://nine.websudoku.com/?')
    time.sleep(1)
    driver.maximize_window()

    driver.get_screenshot_as_file(file_name)
    img = process_image_file(file_name)
    first_cell = driver.find_elements(By.ID, 'f00')
    try:
        while True:
            pass  # Do something
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    start()
