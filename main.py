#######################################################################################################################
# File: main.py
#
#######################################################################################################################
#imports
import os
import time
from config_file import file_name
from image_processing import process_image_file
import numpy as np
from sudoku_solver import Solver
from board import Board

#constants

if __name__ == '__main__':
    sudoku_solver = Solver()
    sudoku_solver.set_difficulty()
    first_run = True
    try:
        while True:
            size_and_loc = sudoku_solver.next_puzzle()
            puzzle = process_image_file(file_name, size_and_loc)
            puzzle_board = Board(puzzle)
            sudoku_solver.solve(puzzle_board)
            first_run = False
    except KeyboardInterrupt:
        pass


