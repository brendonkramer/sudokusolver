import numpy as np
from board import Board

puzzle = np.matrix([[0, 0, 3, 0, 2, 0, 6, 0, 0],
                    [9, 0, 0, 3, 0, 5, 0, 0, 1],
                    [0, 0, 1, 8, 0, 6, 4, 0, 0],
                    [0, 0, 8, 1, 0, 2, 9, 0, 0],
                    [7, 0, 0, 0, 0, 0, 0, 0, 8],
                    [0, 0, 6, 7, 0, 8, 2, 0, 0],
                    [0, 0, 2, 6, 0, 9, 5, 0, 0],
                    [8, 0, 0, 2, 0, 3, 0, 0, 9],
                    [0, 0, 5, 0, 1, 0, 3, 0, 0]])

# puzzle = np.matrix([[0, 0, 0, 8, 0, 0, 9, 0, 0],
#                     [0, 7, 0, 0, 9, 0, 0, 0, 1],
#                     [0, 0, 0, 0, 0, 5, 4, 7, 0],
#                     [3, 5, 0, 0, 4, 0, 2, 0, 0],
#                     [7, 0, 9, 0, 0, 3, 6, 8, 5],
#                     [0, 0, 2, 0, 0, 9, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 8],
#                     [0, 6, 0, 0, 5, 0, 0, 0, 0],
#                     [0, 0, 4, 6, 3, 8, 1, 0, 0]])

board = Board(puzzle)
print(board.get_layout())


board.calculate_definite_elim(first_run=True)

while board.get_blanks() > 0:
    prev_blanks = board.get_blanks()
    board.calculate_definite_elim()
    board.calculate_single_instances()
    if prev_blanks == board.get_blanks():
        break;



#board.solve()

# algo 2
# while board.get_blanks() > 0:
#     for y in range(9):
#         for x in range(9):
#             board.calculate_domain(x, y)
#     board.definite_elim()

# algo 1
# zero_count = 0
# for y in range(9):
#     for x in range(9):
#         if board.get_layout()[y, x] == 0:
#             zero_count = zero_count + 1
# while zero_count != 0:
#     for y in range(9):
#         for x in range(9):
#             if board.get_layout()[y, x] == 0:
#                 if len(board.get_domain(x, y)) == 1:
#                     print(x)
#                     print(y)
#                     answer = board.get_domain(x, y)
#                     print(answer)
#                     board.get_layout()[y, x] = answer[0]
#                     zero_count = zero_count - 1

print(board.get_layout())