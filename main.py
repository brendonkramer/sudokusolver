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
import numpy as np
from board import Board

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


# puzzle = np.matrix([[0, 0, 3, 0, 2, 0, 6, 0, 0],
#                     [9, 0, 0, 3, 0, 5, 0, 0, 1],
#                     [0, 0, 1, 8, 0, 6, 4, 0, 0],
#                     [0, 0, 8, 1, 0, 2, 9, 0, 0],
#                     [7, 0, 0, 0, 0, 0, 0, 0, 8],
#                     [0, 0, 6, 7, 0, 8, 2, 0, 0],
#                     [0, 0, 2, 6, 0, 9, 5, 0, 0],
#                     [8, 0, 0, 2, 0, 3, 0, 0, 9],
#                     [0, 0, 5, 0, 1, 0, 3, 0, 0]])
#
# board = Board(puzzle)
# print(board.get_layout())
# zero_count = 0
# for y in range(9):
#     for x in range(9):
#         if board.get_layout()[y, x] == 0:
#             zero_count = zero_count + 1
#
# while zero_count != 0:
#     for y in range(9):
#         for x in range(9):
#             if board.get_layout()[y,x] == 0:
#                 if len(board.get_domain(x,y)) == 1:
#                     print(x)
#                     print(y)
#                     answer = board.get_domain(x,y)
#                     print(answer)
#                     board.get_layout()[y,x] = answer[0]
#                     zero_count = zero_count - 1
#
# print(board.get_layout())
