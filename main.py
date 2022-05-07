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
    try:
        while True:
            puzzle = process_image_file(file_name)
            puzzle_board = Board(puzzle)
            sudoku_solver.solve(puzzle)
            sudoku_solver.next_puzzle()
    except KeyboardInterrupt:
        pass

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

