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
        print(puzzle.get_layout())
        zero_count = 0
        for y in range(9):
            for x in range(9):
                if puzzle.get_layout()[y, x] == 0:
                    zero_count = zero_count + 1

        while zero_count != 0:
            for y in range(9):
                for x in range(9):
                    if puzzle.get_layout()[y,x] == 0:
                        if len(puzzle.get_domain(x,y)) == 1:
                            print(x)
                            print(y)
                            answer = puzzle.get_domain(x,y)
                            print(answer)
                            puzzle.get_layout()[y,x] = answer[0]
                            zero_count = zero_count - 1

        print(puzzle.get_layout())

    def next_puzzle(self):
        #next puzzle
        self._sudoku_driver.save_screen()
        return self._sudoku_driver.get_size_and_loc()