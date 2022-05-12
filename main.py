#######################################################################################################################
# File: main.py
#
#######################################################################################################################
# imports
import os
import time
from config_file import file_name
from image_processing import process_image_file
import numpy as np
from sudoku_solver import Solver
from board import Board

# constants

if __name__ == '__main__':
    sudoku_solver = Solver()
    #sudoku_solver.set_difficulty()
    first_run = True
    try:
        while True:
            #size_and_loc = sudoku_solver.next_puzzle()
            #puzzle = process_image_file(file_name, size_and_loc)
            puzzle = np.matrix([[4, 0, 0, 0, 0, 0, 7, 0, 0],
                                [0, 2, 6, 0, 9, 0, 0, 0, 4],
                                [5, 0, 0, 8, 6, 4, 0, 2, 0],
                                [2, 0, 8, 0, 0, 1, 0, 4, 0],
                                [6, 9, 3, 0, 0, 8, 2, 0, 0],
                                [0, 0, 0, 0, 2, 6, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 9],
                                [3, 1, 0, 0, 8, 9, 0, 0, 2],
                                [9, 0, 0, 0, 5, 0, 0, 7, 8]])
            puzzle_board = Board(puzzle)
            sudoku_solver.solve(puzzle_board)
            first_run = False
    except KeyboardInterrupt:
        pass
