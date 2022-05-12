#######################################################################################################################
# File: website_driver.py
#
#######################################################################################################################

# imports
import sys
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
            prev_blanks = puzzle.get_blanks()
            puzzle.calculate_definite_elim()
            puzzle.calculate_single_instances()
            puzzle.calculate_naked_n(3)
            puzzle.calculate_naked_n(4)
            puzzle.calculate_naked_n(5)
            #print("\nPUZZLE Calc")
            #print(puzzle.get_layout())
            #print("\nDOMAIN Calc")
            #puzzle.get_domain_all()
            if prev_blanks == puzzle.get_blanks():
                puzzle.find_pointing_pairs()
                #print("\nDOMAIN Point Pairs")
                #puzzle.get_domain_all()
                puzzle.find_naked_doubles()
                puzzle.calculate_definite_elim()
                puzzle.calculate_single_instances()
                prev_blanks = puzzle.get_blanks()
                if prev_blanks == puzzle.get_blanks():
                    print("\nBACK TRACK")
                    if not self.back_track(puzzle):
                        sys.exit("backtrack failed")
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

    def is_possible_to_place(self, puzzle, row, col, val):
        for j in range(0, 9):
            if puzzle.get_layout()[row, j] == val:
                return False

        for i in range(0, 9):
            if puzzle.get_layout()[i, col] == val:
                return False

        startRow = (row // 3) * 3
        startCol = (col // 3) * 3
        for row in range(startRow, startRow + 3):
            for col in range(startCol, startCol + 3):
                if puzzle.get_layout()[startRow, startCol] == val:
                    return False

        return True

    def back_track(self, puzzle):
        for row in range(0, 9):
            for col in range(0, 9):
                cell = puzzle.get_layout()[row, col]
                if cell == 0:
                    domain = puzzle.get_domain(col, row)
                    for val in domain:
                        if self.is_possible_to_place(puzzle,col, row,val):
                            puzzle.get_layout()[col, row] = val
                            #puzzle.place(val, col, row)
                            print(puzzle.get_layout())
                            if self.back_track(puzzle):
                                return True
                            # Bad choice, make it blank and check again
                            puzzle.get_layout()[col, row] = 0
        return False
        print(puzzle.get_layout())