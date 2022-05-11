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
        count = 1
        while puzzle.get_blanks() > 0:
            for y in range(9):
                for x in range(9):
                    puzzle.calculate_definite_elim(x, y)
            for y in range(3):
                for x in range(3):
                    puzzle.find_pointing_pairs(x, y)
            print("RUN " + str(count))
            count += 1
            print("PUZZLE \n")
            print(puzzle.get_layout())
            print("DOMAIN \n")
            print(puzzle.get_domain_all())
        for y in range(9):
            for x in range(9):
                self._sudoku_driver.set_value(x,y,puzzle.get_layout[y][x])
        print(puzzle.get_layout())
        self._sudoku_driver.submit()

    def next_puzzle(self):
        self._sudoku_driver.save_screen()
        return self._sudoku_driver.get_size_and_loc()

    def set_difficulty(self):
        self._sudoku_driver.set_difficulty()
