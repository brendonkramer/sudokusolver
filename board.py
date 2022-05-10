#######################################################################################################################
# File: board.py
#
#######################################################################################################################

# imports
import numpy as np


#######################################################################################################################
# Class: Board
#######################################################################################################################
class Board:
    """
  Board instance
  """

    def __init__(self, layout, parent=None, score=None):
        """
    Constructor for Board
    :param layout: board layout to associate to this Board instance
    :type layout: 2D array
    :param parent: parent of this board instance
    :type parent: Board
    :param score: score used for A*
    :type score: int
    """
        self._layout = layout
        self._children = []
        self._siblings = []
        self._parent = parent
        self._score = score
        # self._domains = np.empty([9, 9])
        # self._domains.astype('O')
        self._domains = [[[],[],[],[],[],[],[],[],[]],
                         [[],[],[],[],[],[],[],[],[]],
                         [[],[],[],[],[],[],[],[],[]],
                         [[],[],[],[],[],[],[],[],[]],
                         [[],[],[],[],[],[],[],[],[]],
                         [[],[],[],[],[],[],[],[],[]],
                         [[],[],[],[],[],[],[],[],[]],
                         [[],[],[],[],[],[],[],[],[]],
                         [[],[],[],[],[],[],[],[],[]]]
        self._blanks = 81
        for y in range(9):
            for x in range(9):
                if layout[y, x] != 0:
                    self._blanks = self._blanks - 1

    #######################################################################################################################
    # Function: find_blank
    #######################################################################################################################
    def find_blank(self):
        """
    Finds blank tile in the 2d array of this Board
    :return: index of blank
    :rtype: int
    """
        index = None
        for row in range(len(self._layout)):
            for col in range(len(self._layout[row])):
                if (self._layout[row][col] == 0):
                    index = [row, col]
        return index

    #######################################################################################################################
    # Function: get_layout
    #######################################################################################################################
    def get_layout(self):
        """
    Returns this boards layout
    :return: this boards layout
    :rtype: 2d array
    """
        return self._layout

    #######################################################################################################################
    # Function: add_child
    #######################################################################################################################
    def add_child(self, child):
        """
    Adds children to the current node for linking
    :param child: child to add to a list in this Board
    :type child: Board
    :return: None
    """
        self._children.append(child)

    #######################################################################################################################
    # Function: num_parents
    #######################################################################################################################
    def num_parents(self):
        """
    Return the number of parents associated to this board
    :return: the number of parents associated to this board
    :rtype: int
    """
        num_moves = 0
        state = self
        while (state is not None):
            state = state._parent
            num_moves += 1
        return num_moves

    #######################################################################################################################
    # Function: generate_score
    #######################################################################################################################
    def generate_score(self, goal):
        """
    Generate the manhattan distance + current moves and return it
    :param goal: goal Board
    :type goal: Board
    :return: the manhattan distance + current moves
    :rtype: int
    """
        goal_layout = goal.get_layout()
        count = 0
        this_row = 0
        while this_row < 3:
            this_col = 0
            while this_col < 3:
                goal_row = 0
                while goal_row < 3:
                    goal_col = 0
                    while goal_col < 3:
                        if (self._layout[this_row][this_col] == goal_layout[goal_row][goal_col]):
                            count += (abs(this_row - goal_row) + abs(this_col - goal_col))
                        goal_col += 1
                    goal_row += 1
                this_col += 1
            this_row += 1
        self._score = count + self.num_parents()

    def solve(self):
        while self._blanks > 1:
            for y in range(9):
                for x in range(9):
                    self.calculate_definite_elim(x, y)

    def get_blanks(self):
        return self._blanks

    def calculate_definite_elim(self, x_index, y_index):
        domain_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(9):
            if self._layout[y_index, x] != 0:
                if self._layout[y_index, x] in domain_list:
                    domain_list.remove(self._layout[y_index, x])
        for y in range(9):
            if self._layout[y, x_index] != 0:
                if self._layout[y, x_index] in domain_list:
                    domain_list.remove(self._layout[y, x_index])
        if x_index < 3 and y_index < 3:
            for y in range(3):
                for x in range(3):
                    if self._layout[y, x] != 0:
                        if self._layout[y, x] in domain_list:
                            domain_list.remove(self._layout[y, x])
        if 2 < x_index < 6 and y_index < 3:
            for y in range(3):
                for x in range(3):
                    if self._layout[y, x + 3] != 0:
                        if self._layout[y, x + 3] in domain_list:
                            domain_list.remove(self._layout[y, x + 3])
        if x_index > 5 and y_index < 3:
            for y in range(3):
                for x in range(3):
                    if self._layout[y, x + 6] != 0:
                        if self._layout[y, x + 6] in domain_list:
                            domain_list.remove(self._layout[y, x + 6])
        if x_index < 3 and 2 < y_index < 6:
            for y in range(3):
                for x in range(3):
                    if self._layout[y + 3, x] != 0:
                        if self._layout[y + 3, x] in domain_list:
                            domain_list.remove(self._layout[y + 3, x])
        if 2 < x_index < 6 and 2 < y_index < 6:
            for y in range(3):
                for x in range(3):
                    if self._layout[y + 3, x + 3] != 0:
                        if self._layout[y + 3, x + 3] in domain_list:
                            domain_list.remove(self._layout[y + 3, x + 3])
        if x_index > 5 and 2 < y_index < 6:
            for y in range(3):
                for x in range(3):
                    if self._layout[y + 3, x + 6] != 0:
                        if self._layout[y + 3, x + 6] in domain_list:
                            domain_list.remove(self._layout[y + 3, x + 6])
        if x_index < 3 and y_index > 5:
            for y in range(3):
                for x in range(3):
                    if self._layout[y + 6, x] != 0:
                        if self._layout[y + 6, x] in domain_list:
                            domain_list.remove(self._layout[y + 6, x])
        if 2 < x_index < 6 and y_index > 5:
            for y in range(3):
                for x in range(3):
                    if self._layout[y + 6, x + 3] != 0:
                        if self._layout[y + 6, x + 3] in domain_list:
                            domain_list.remove(self._layout[y + 6, x + 3])
        if x_index > 5 and y_index > 5:
            for y in range(3):
                for x in range(3):
                    if self._layout[y + 6, x + 6] != 0:
                        if self._layout[y + 6, x + 6] in domain_list:
                            domain_list.remove(self._layout[y + 6, x + 6])

        #print(domain_list)
        if len(domain_list) == 1:
            if self._layout[y_index, x_index] != 0:
                self._layout[y, x] = domain_list[0]
                self._blanks -= 1
                domain_list = []
        self._domains[y_index][x_index] = domain_list


    def calculate_single_instances(self):
        domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for y in range(9):
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(9):
                for num in self._domains[y][x]:
                    if num == 1:
                        domain_count_list[0] += 1
                    elif num == 2:
                        domain_count_list[1] += 1
                    elif num == 3:
                        domain_count_list[2] += 1
                    elif num == 4:
                        domain_count_list[3] += 1
                    elif num == 5:
                        domain_count_list[4] += 1
                    elif num == 6:
                        domain_count_list[5] += 1
                    elif num == 7:
                        domain_count_list[6] += 1
                    elif num == 8:
                        domain_count_list[7] += 1
                    elif num == 9:
                        domain_count_list[8] += 1
                for i in range(len(domain_count_list)):
                    if domain_count_list[i] == 1:
                        self._domains[y][x] = []
                        self._layout[y, x] = i

        for x in range(9):
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(9):
                for num in self._domains[y][x]:
                    if num == 1:
                        domain_count_list[0] += 1
                    elif num == 2:
                        domain_count_list[1] += 1
                    elif num == 3:
                        domain_count_list[2] += 1
                    elif num == 4:
                        domain_count_list[3] += 1
                    elif num == 5:
                        domain_count_list[4] += 1
                    elif num == 6:
                        domain_count_list[5] += 1
                    elif num == 7:
                        domain_count_list[6] += 1
                    elif num == 8:
                        domain_count_list[7] += 1
                    elif num == 9:
                        domain_count_list[8] += 1
                for i in range(len(domain_count_list)):
                    if domain_count_list[i] == 1:
                        self._domains[y][x] = []
                        self._layout[y, x] = i

        if x_index < 3 and y_index < 3:
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(3):
                for x in range(3):
                    for num in self._domains[y][x]:
                        if num == 1:
                            domain_count_list[0] += 1
                        elif num == 2:
                            domain_count_list[1] += 1
                        elif num == 3:
                            domain_count_list[2] += 1
                        elif num == 4:
                            domain_count_list[3] += 1
                        elif num == 5:
                            domain_count_list[4] += 1
                        elif num == 6:
                            domain_count_list[5] += 1
                        elif num == 7:
                            domain_count_list[6] += 1
                        elif num == 8:
                            domain_count_list[7] += 1
                        elif num == 9:
                            domain_count_list[8] += 1
            for i in range(len(domain_count_list)):
                if domain_count_list[i] == 1:
                    self._domains[y][x] = []
                    self._layout[y, x] = i

        if 2 < x_index < 6 and y_index < 3:
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(3):
                for x in range(3, 6):
                    for num in self._domains[y][x]:
                        if num == 1:
                            domain_count_list[0] += 1
                        elif num == 2:
                            domain_count_list[1] += 1
                        elif num == 3:
                            domain_count_list[2] += 1
                        elif num == 4:
                            domain_count_list[3] += 1
                        elif num == 5:
                            domain_count_list[4] += 1
                        elif num == 6:
                            domain_count_list[5] += 1
                        elif num == 7:
                            domain_count_list[6] += 1
                        elif num == 8:
                            domain_count_list[7] += 1
                        elif num == 9:
                            domain_count_list[8] += 1
            for i in range(len(domain_count_list)):
                if domain_count_list[i] == 1:
                    self._domains[y][x] = []
                    self._layout[y, x] = i

        if x_index > 5 and y_index < 3:
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(3):
                for x in range(6, 9):
                    for num in self._domains[y][x]:
                        if num == 1:
                            domain_count_list[0] += 1
                        elif num == 2:
                            domain_count_list[1] += 1
                        elif num == 3:
                            domain_count_list[2] += 1
                        elif num == 4:
                            domain_count_list[3] += 1
                        elif num == 5:
                            domain_count_list[4] += 1
                        elif num == 6:
                            domain_count_list[5] += 1
                        elif num == 7:
                            domain_count_list[6] += 1
                        elif num == 8:
                            domain_count_list[7] += 1
                        elif num == 9:
                            domain_count_list[8] += 1
            for i in range(len(domain_count_list)):
                if domain_count_list[i] == 1:
                    self._domains[y][x] = []
                    self._layout[y, x] = i

        if x_index < 3 and 2 < y_index < 6:
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(3, 6):
                for x in range(3):
                    for num in self._domains[y][x]:
                        if num == 1:
                            domain_count_list[0] += 1
                        elif num == 2:
                            domain_count_list[1] += 1
                        elif num == 3:
                            domain_count_list[2] += 1
                        elif num == 4:
                            domain_count_list[3] += 1
                        elif num == 5:
                            domain_count_list[4] += 1
                        elif num == 6:
                            domain_count_list[5] += 1
                        elif num == 7:
                            domain_count_list[6] += 1
                        elif num == 8:
                            domain_count_list[7] += 1
                        elif num == 9:
                            domain_count_list[8] += 1
            for i in range(len(domain_count_list)):
                if domain_count_list[i] == 1:
                    self._domains[y][x] = []
                    self._layout[y, x] = i

        if 2 < x_index < 6 and 2 < y_index < 6:
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(3, 6):
                for x in range(3, 6):
                    for num in self._domains[y][x]:
                        if num == 1:
                            domain_count_list[0] += 1
                        elif num == 2:
                            domain_count_list[1] += 1
                        elif num == 3:
                            domain_count_list[2] += 1
                        elif num == 4:
                            domain_count_list[3] += 1
                        elif num == 5:
                            domain_count_list[4] += 1
                        elif num == 6:
                            domain_count_list[5] += 1
                        elif num == 7:
                            domain_count_list[6] += 1
                        elif num == 8:
                            domain_count_list[7] += 1
                        elif num == 9:
                            domain_count_list[8] += 1
            for i in range(len(domain_count_list)):
                if domain_count_list[i] == 1:
                    self._domains[y][x] = []
                    self._layout[y, x] = i

        if x_index > 5 and 2 < y_index < 6:
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(3, 6):
                for x in range(6, 9):
                    for num in self._domains[y][x]:
                        if num == 1:
                            domain_count_list[0] += 1
                        elif num == 2:
                            domain_count_list[1] += 1
                        elif num == 3:
                            domain_count_list[2] += 1
                        elif num == 4:
                            domain_count_list[3] += 1
                        elif num == 5:
                            domain_count_list[4] += 1
                        elif num == 6:
                            domain_count_list[5] += 1
                        elif num == 7:
                            domain_count_list[6] += 1
                        elif num == 8:
                            domain_count_list[7] += 1
                        elif num == 9:
                            domain_count_list[8] += 1
            for i in range(len(domain_count_list)):
                if domain_count_list[i] == 1:
                    self._domains[y][x] = []
                    self._layout[y, x] = i

        if x_index < 3 and y_index > 5:
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(6, 9):
                for x in range(3):
                    for num in self._domains[y][x]:
                        if num == 1:
                            domain_count_list[0] += 1
                        elif num == 2:
                            domain_count_list[1] += 1
                        elif num == 3:
                            domain_count_list[2] += 1
                        elif num == 4:
                            domain_count_list[3] += 1
                        elif num == 5:
                            domain_count_list[4] += 1
                        elif num == 6:
                            domain_count_list[5] += 1
                        elif num == 7:
                            domain_count_list[6] += 1
                        elif num == 8:
                            domain_count_list[7] += 1
                        elif num == 9:
                            domain_count_list[8] += 1
            for i in range(len(domain_count_list)):
                if domain_count_list[i] == 1:
                    self._domains[y][x] = []
                    self._layout[y, x] = i

        if 2 < x_index < 6 and y_index > 5:
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(6, 9):
                for x in range(3, 6):
                    for num in self._domains[y][x]:
                        if num == 1:
                            domain_count_list[0] += 1
                        elif num == 2:
                            domain_count_list[1] += 1
                        elif num == 3:
                            domain_count_list[2] += 1
                        elif num == 4:
                            domain_count_list[3] += 1
                        elif num == 5:
                            domain_count_list[4] += 1
                        elif num == 6:
                            domain_count_list[5] += 1
                        elif num == 7:
                            domain_count_list[6] += 1
                        elif num == 8:
                            domain_count_list[7] += 1
                        elif num == 9:
                            domain_count_list[8] += 1
            for i in range(len(domain_count_list)):
                if domain_count_list[i] == 1:
                    self._domains[y][x] = []
                    self._layout[y, x] = i

        if x_index > 5 and y_index > 5:
            domain_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(6, 9):
                for x in range(6, 9):
                    for num in self._domains[y][x]:
                        if num == 1:
                            domain_count_list[0] += 1
                        elif num == 2:
                            domain_count_list[1] += 1
                        elif num == 3:
                            domain_count_list[2] += 1
                        elif num == 4:
                            domain_count_list[3] += 1
                        elif num == 5:
                            domain_count_list[4] += 1
                        elif num == 6:
                            domain_count_list[5] += 1
                        elif num == 7:
                            domain_count_list[6] += 1
                        elif num == 8:
                            domain_count_list[7] += 1
                        elif num == 9:
                            domain_count_list[8] += 1
            for i in range(len(domain_count_list)):
                if domain_count_list[i] == 1:
                    self._domains[y][x] = []
                    self._layout[y, x] = i


    def get_domain(self, x, y):
        return self._domains[y][x]

    def definite_elim(self):
        for y in range(9):
            for x in range(9):
                if len(self._domains[y][x]) == 1:
                    if self._layout[y, x] == 0:
                        self._layout[y, x] = self._domains[y][x][0]
                        self._blanks -= 1

    # def get_naked_doubles(self):
    #   # rows
    #   # doubles_list = []
    #   # for x in range(9):
    #   #   if (len(self.get_domain(x,0)) == 2):
    #   #     doubles_list.append(self.get_domain(x,0))
    #   # for double in doubles_list:
    #   #   count = 0
    #   #   for double_2 in doubles_list:
    #   #     if double == double_2:
    #   #       count = count + 1
    #   #   if count == 2:
    #   #     #TODO add list of domains to this class
    #   return false

    #######################################################################################################################
    # Function: get_score
    #######################################################################################################################
    def get_score(self):
        """
    Return current score
    :return: current score
    :rtype: int
    """
        return self._score
