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
        puzzle.calculate_definite_elim(True)
        print("\nPUZZLE 1")
        print(puzzle.get_layout())
        print("\nDOMAIN 1")
        puzzle.get_domain_all()
        while puzzle.get_blanks() > 0:
            puzzle.calculate_definite_elim()
            print("\nPUZZLE Calc")
            print(puzzle.get_layout())
            print("\nDOMAIN Calc")
            puzzle.get_domain_all()
            puzzle.find_pointing_pairs()
            print("\nDOMAIN Point Pairs")
            puzzle.get_domain_all()
            puzzle.calculate_definite_elim()
            puzzle.find_naked_doubles()
            print("RUN " + str(count))
            count += 1
            print("PUZZLE End Loop\n")
            print(puzzle.get_layout())
        for y in range(9):
            for x in range(9):
                self._sudoku_driver.set_value(x,y,puzzle.get_layout()[y][x])
        print(puzzle.get_layout())
        self._sudoku_driver.submit()

    def next_puzzle(self):
        self._sudoku_driver.save_screen()
        return self._sudoku_driver.get_size_and_loc()

    def set_difficulty(self):
        self._sudoku_driver.set_difficulty()
