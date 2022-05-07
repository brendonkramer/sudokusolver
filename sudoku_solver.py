#######################################################################################################################
# File: website_driver.py
#
#######################################################################################################################

# imports
import time
from website_driver import Driver

class Solver():

    def __init__(self):
        self._sudoku_driver = Driver()
        self._sudoku_driver.start()

    def solve(self, puzzle):
        self._puzzle = puzzle

    def next_puzzle(self):
        #next puzzle
        self._sudoku_driver.save_screen()
        return self._sudoku_driver.get_size_and_loc()