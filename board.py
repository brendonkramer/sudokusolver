#######################################################################################################################
# File: board.py
#
#######################################################################################################################

# imports
import numpy as np
import itertools

#######################################################################################################################
# Class: Board
#######################################################################################################################
class Board:
    """
  Board instance
  """

    def __init__(self, layout):
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

    def get_blanks(self):
        return self._blanks

    def place(self, num, x_index, y_index):
        self._layout[y_index, x_index] = num
        self._domains[y_index][x_index] = []
        self._blanks -= 1
        for x in range(9):
            if num in self._domains[y_index][x]:
                self._domains[y_index][x].remove(num)
        for y in range(9):
            if num in self._domains[y][x_index]:
                self._domains[y][x_index].remove(num)

        if x_index < 3 and y_index < 3:
            for y in range(3):
                for x in range(3):
                    if num in self._domains[y][x]:
                        self._domains[y][x].remove(num)
        # box 2
        if 2 < x_index < 6 and y_index < 3:
            for y in range(3):
                for x in range(3, 6):
                    if num in self._domains[y][x]:
                        self._domains[y][x].remove(num)
        # box 3
        if x_index > 5 and y_index < 3:
            for y in range(3):
                for x in range(6, 9):
                    if num in self._domains[y][x]:
                        self._domains[y][x].remove(num)
        # box 4
        if x_index < 3 and 2 < y_index < 6:
            for y in range(3, 6):
                for x in range(3):
                    if num in self._domains[y][x]:
                        self._domains[y][x].remove(num)
        # box 5
        if 2 < x_index < 6 and 2 < y_index < 6:
            for y in range(3, 6):
                for x in range(3, 6):
                    if num in self._domains[y][x]:
                        self._domains[y][x].remove(num)
        # box 6
        if x_index > 5 and 2 < y_index < 6:
            for y in range(3, 6):
                for x in range(6, 9):
                    if num in self._domains[y][x]:
                        self._domains[y][x].remove(num)
        # box 7
        if x_index < 3 and y_index > 5:
            for y in range(6, 9):
                for x in range(3):
                    if num in self._domains[y][x]:
                        self._domains[y][x].remove(num)
        # box 8
        if 2 < x_index < 6 and y_index > 5:
            for y in range(6, 9):
                for x in range(3, 6):
                    if num in self._domains[y][x]:
                        self._domains[y][x].remove(num)
        # box 9
        if x_index > 5 and y_index > 5:
            for y in range(6, 9):
                for x in range(6, 9):
                    if num in self._domains[y][x]:
                        self._domains[y][x].remove(num)


    def calculate_definite_elim(self, first_run = False):
        for y_index in range(9):
            for x_index in range(9):
                if self._layout[y_index, x_index] == 0:
                    if first_run is True:
                        domain_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    else:
                        domain_list = self._domains[y_index][x_index]
                    for x in range(9):
                        if self._layout[y_index, x] != 0:
                            if self._layout[y_index, x] in domain_list:
                                domain_list.remove(self._layout[y_index, x])
                    for y in range(9):
                        if self._layout[y, x_index] != 0:
                            if self._layout[y, x_index] in domain_list:
                                domain_list.remove(self._layout[y, x_index])
                    #box 1
                    if x_index < 3 and y_index < 3:
                        for y in range(3):
                            for x in range(3):
                                if self._layout[y, x] != 0:
                                    if self._layout[y, x] in domain_list:
                                        domain_list.remove(self._layout[y, x])
                    #box 2
                    if 2 < x_index < 6 and y_index < 3:
                        for y in range(3):
                            for x in range(3):
                                if self._layout[y, x + 3] != 0:
                                    if self._layout[y, x + 3] in domain_list:
                                        domain_list.remove(self._layout[y, x + 3])
                    #box 3
                    if x_index > 5 and y_index < 3:
                        for y in range(3):
                            for x in range(3):
                                if self._layout[y, x + 6] != 0:
                                    if self._layout[y, x + 6] in domain_list:
                                        domain_list.remove(self._layout[y, x + 6])
                    #box 4
                    if x_index < 3 and 2 < y_index < 6:
                        for y in range(3):
                            for x in range(3):
                                if self._layout[y + 3, x] != 0:
                                    if self._layout[y + 3, x] in domain_list:
                                        domain_list.remove(self._layout[y + 3, x])
                    #box 5
                    if 2 < x_index < 6 and 2 < y_index < 6:
                        for y in range(3):
                            for x in range(3):
                                if self._layout[y + 3, x + 3] != 0:
                                    if self._layout[y + 3, x + 3] in domain_list:
                                        domain_list.remove(self._layout[y + 3, x + 3])
                    #box 6
                    if x_index > 5 and 2 < y_index < 6:
                        for y in range(3):
                            for x in range(3):
                                if self._layout[y + 3, x + 6] != 0:
                                    if self._layout[y + 3, x + 6] in domain_list:
                                        domain_list.remove(self._layout[y + 3, x + 6])
                    #box 7
                    if x_index < 3 and y_index > 5:
                        for y in range(3):
                            for x in range(3):
                                if self._layout[y + 6, x] != 0:
                                    if self._layout[y + 6, x] in domain_list:
                                        domain_list.remove(self._layout[y + 6, x])
                    #box 8
                    if 2 < x_index < 6 and y_index > 5:
                        for y in range(3):
                            for x in range(3):
                                if self._layout[y + 6, x + 3] != 0:
                                    if self._layout[y + 6, x + 3] in domain_list:
                                        domain_list.remove(self._layout[y + 6, x + 3])
                    #box 9
                    if x_index > 5 and y_index > 5:
                        for y in range(3):
                            for x in range(3):
                                if self._layout[y + 6, x + 6] != 0:
                                    if self._layout[y + 6, x + 6] in domain_list:
                                        domain_list.remove(self._layout[y + 6, x + 6])

                    if len(domain_list) == 1:
                        self.place(domain_list[0],x_index,y_index)
                        domain_list = []
                    self._domains[y_index][x_index] = domain_list
                # print(y_index, end=",")
                # print(x_index, end=",")
                # print(self._domains[y_index][x_index])

    def calculate_single_instances(self):
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
            for i in range(9):
                if domain_count_list[i] == 1:
                    for x in range(9):
                        if i+1 in self._domains[y][x]:
                            self.place(i+1, x, y)

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
            for i in range(9):
                if domain_count_list[i] == 1:
                    for y in range(9):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

        #first box
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
        for i in range(9):
            if domain_count_list[i] == 1:
                for y in range(3):
                    for x in range(3):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

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
        for i in range(9):
            if domain_count_list[i] == 1:
                for y in range(3):
                    for x in range(3, 6):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

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
        for i in range(9):
            if domain_count_list[i] == 1:
                for y in range(3):
                    for x in range(6, 9):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

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
        for i in range(9):
            if domain_count_list[i] == 1:
                for y in range(3, 6):
                    for x in range(3):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

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
        for i in range(9):
            if domain_count_list[i] == 1:
                for y in range(3, 6):
                    for x in range(3, 6):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

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
        for i in range(9):
            if domain_count_list[i] == 1:
                for y in range(3, 6):
                    for x in range(6, 9):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

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
        for i in range(9):
            if domain_count_list[i] == 1:
                for y in range(6, 9):
                    for x in range(3):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

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
        for i in range(9):
            if domain_count_list[i] == 1:
                for y in range(6, 9):
                    for x in range(3, 6):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

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
        for i in range(9):
            if domain_count_list[i] == 1:
                for y in range(6, 9):
                    for x in range(6, 9):
                        if i + 1 in self._domains[y][x]:
                            self.place(i+1, x, y)

    def calculate_naked_n(self, n):
        # rows
        for y in range(9):
            collective_domain_set = set()
            for x in range(9):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
            subset_list = list(itertools.combinations(collective_domain_set,n))
            for subset in subset_list:
                count = 0
                n_size_groups_index_list = []
                for x in range(9):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_groups_index_list.append(x)
                if count == n:
                    # oooo baby a triple
                    for x in range(9):
                        if x not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1
        # columns
        for x in range(9):
            collective_domain_set = set()
            for y in range(9):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
            subset_list = list(itertools.combinations(collective_domain_set,n))
            for subset in subset_list:
                count = 0
                n_size_groups_index_list = []
                for y in range(9):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_groups_index_list.append(y)
                if count == n:
                    # oooo baby a triple
                    for y in range(9):
                        if y not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

        #box 1
        collective_domain_set = set()
        for y in range(3):
            for x in range(3):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
        subset_list = list(itertools.combinations(collective_domain_set, n))
        for subset in subset_list:
            count = 0
            n_size_groups_index_list = []
            for y in range(3):
                for x in range(3):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_group_index = [y, x]
                            n_size_groups_index_list.append(n_size_group_index)
            if count == n:
                # oooo baby a triple
                for y in range(3):
                    for x in range(3):
                        index_pair = [y, x]
                        if index_pair not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

        # box 2
        collective_domain_set = set()
        for y in range(3):
            for x in range(3, 6):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
        subset_list = list(itertools.combinations(collective_domain_set, n))
        for subset in subset_list:
            count = 0
            n_size_groups_index_list = []
            for y in range(3):
                for x in range(3, 6):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_group_index = [y, x]
                            n_size_groups_index_list.append(n_size_group_index)
            if count == n:
                # oooo baby a triple
                for y in range(3):
                    for x in range(3, 6):
                        index_pair = [y, x]
                        if index_pair not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

        # box 3
        collective_domain_set = set()
        for y in range(3):
            for x in range(6, 9):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
        subset_list = list(itertools.combinations(collective_domain_set, n))
        for subset in subset_list:
            count = 0
            n_size_groups_index_list = []
            for y in range(3):
                for x in range(6, 9):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_group_index = [y, x]
                            n_size_groups_index_list.append(n_size_group_index)
            if count == n:
                # oooo baby a triple
                for y in range(3):
                    for x in range(6, 9):
                        index_pair = [y, x]
                        if index_pair not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

        # box 4
        collective_domain_set = set()
        for y in range(3, 6):
            for x in range(3):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
        subset_list = list(itertools.combinations(collective_domain_set, n))
        for subset in subset_list:
            count = 0
            n_size_groups_index_list = []
            for y in range(3, 6):
                for x in range(3):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_group_index = [y, x]
                            n_size_groups_index_list.append(n_size_group_index)
            if count == n:
                # oooo baby a triple
                for y in range(3, 6):
                    for x in range(3):
                        index_pair = [y, x]
                        if index_pair not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

        # box 5
        collective_domain_set = set()
        for y in range(3, 6):
            for x in range(3, 6):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
        subset_list = list(itertools.combinations(collective_domain_set, n))
        for subset in subset_list:
            count = 0
            n_size_groups_index_list = []
            for y in range(3, 6):
                for x in range(3, 6):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_group_index = [y, x]
                            n_size_groups_index_list.append(n_size_group_index)
            if count == n:
                # oooo baby a triple
                for y in range(3, 6):
                    for x in range(3, 6):
                        index_pair = [y, x]
                        if index_pair not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

        # box 6
        collective_domain_set = set()
        for y in range(3, 6):
            for x in range(6, 9):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
        subset_list = list(itertools.combinations(collective_domain_set, n))
        for subset in subset_list:
            count = 0
            n_size_groups_index_list = []
            for y in range(3, 6):
                for x in range(6, 9):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_group_index = [y, x]
                            n_size_groups_index_list.append(n_size_group_index)
            if count == n:
                # oooo baby a triple
                for y in range(3, 6):
                    for x in range(6, 9):
                        index_pair = [y, x]
                        if index_pair not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

        # box 7
        collective_domain_set = set()
        for y in range(6, 9):
            for x in range(3):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
        subset_list = list(itertools.combinations(collective_domain_set, n))
        for subset in subset_list:
            count = 0
            n_size_groups_index_list = []
            for y in range(6, 9):
                for x in range(3):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_group_index = [y, x]
                            n_size_groups_index_list.append(n_size_group_index)
            if count == n:
                # oooo baby a triple
                for y in range(6, 9):
                    for x in range(3):
                        index_pair = [y, x]
                        if index_pair not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

        # box 8
        collective_domain_set = set()
        for y in range(6, 9):
            for x in range(3, 6):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
        subset_list = list(itertools.combinations(collective_domain_set, n))
        for subset in subset_list:
            count = 0
            n_size_groups_index_list = []
            for y in range(6, 9):
                for x in range(3, 6):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_group_index = [y, x]
                            n_size_groups_index_list.append(n_size_group_index)
            if count == n:
                # oooo baby a triple
                for y in range(6, 9):
                    for x in range(3, 6):
                        index_pair = [y, x]
                        if index_pair not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

        # box 9
        collective_domain_set = set()
        for y in range(6, 9):
            for x in range(6, 9):
                for num in self._domains[y][x]:
                    if num not in collective_domain_set:
                        collective_domain_set.add(num)
        subset_list = list(itertools.combinations(collective_domain_set, n))
        for subset in subset_list:
            count = 0
            n_size_groups_index_list = []
            for y in range(6, 9):
                for x in range(6, 9):
                    if len(self._domains[y][x]) > 0:
                        if set(self._domains[y][x]).issubset(set(subset)):
                            count += 1
                            n_size_group_index = [y, x]
                            n_size_groups_index_list.append(n_size_group_index)
            if count == n:
                # oooo baby a triple
                for y in range(6, 9):
                    for x in range(6, 9):
                        index_pair = [y, x]
                        if index_pair not in n_size_groups_index_list:
                            i = 0
                            while i < len(self._domains[y][x]):
                                num = self._domains[y][x][i]
                                if num in list(subset):
                                    self._domains[y][x].remove(num)
                                else:
                                    i += 1

    def get_domain(self, x, y):
        return self._domains[y][x]

    def find_pointing_pairs(self, box_x_index, box_y_index):
        # column search

        domain_per_row_in_box = [set(),set(),set()]
        for y in range(3):
            for x in range(3):
                if self._layout[y, x] == 0:
                    for domain in self._domains[y][x]:
                        domain_per_row_in_box[y].add(domain)
        union = set.union(domain_per_row_in_box[0],domain_per_row_in_box[1], domain_per_row_in_box[2])
        intersection = set.intersection(domain_per_row_in_box[0], domain_per_row_in_box[1])
        intersection1 = set.intersection(domain_per_row_in_box[1], domain_per_row_in_box[2])
        intersection2 = set.intersection(domain_per_row_in_box[2], domain_per_row_in_box[0])
        pointing_pairs =  union - set.union(intersection, intersection1, intersection2)
        print(pointing_pairs)
        for pointing_pair in pointing_pairs:
            for index in range(3):
                if pointing_pair in domain_per_row_in_box[index]:
                    self.remove_num_from_row(index + (box_y_index * 3), pointing_pair, box_x_index)
                    break

        domain_per_col_in_box = [set(), set(), set()]
        for x in range(3):
            for y in range(3):
                if self._layout[y, x] == 0:
                    for domain in self._domains[y][x]:
                        domain_per_col_in_box[y].add(domain)
        union = set.union(domain_per_col_in_box[0], domain_per_col_in_box[1], domain_per_col_in_box[2])
        intersection = set.intersection(domain_per_col_in_box[0], domain_per_col_in_box[1])
        intersection1 = set.intersection(domain_per_col_in_box[1], domain_per_col_in_box[2])
        intersection2 = set.intersection(domain_per_col_in_box[2], domain_per_col_in_box[0])
        pointing_pairs = union - set.union(intersection, intersection1, intersection2)
        print(pointing_pairs)
        for pointing_pair in pointing_pairs:
            for index in range(3):
                if pointing_pair in domain_per_col_in_box[index]:
                    self.remove_num_from_col(index + (box_y_index * 3), pointing_pair, box_x_index)
                    break

        self.solve()

    def remove_num_from_row(self, index, num, box_x_index=None):
        count = 0
        for domain in self._domains[index]:
            if box_x_index == 0:
                if count > 2 and num in domain:
                    domain.remove(num)
            if box_x_index == 1:
                if count < 3 or count > 5 and num in domain:
                    domain.remove(num)
            if box_x_index == 2:
                if count < 6 and num in domain:
                    domain.remove(num)
            else:
                domain.remove(num)
            count += 1

    def remove_num_from_col(self, index, num, box_y_index=None):
        count = 0
        for col in range(9):
            domain = self._domains[col][index]
            if box_y_index == 0:
                if count > 2 and num in domain:
                    domain.remove(num)
            if box_y_index == 1:
                if count < 3 or count > 5 and num in domain:
                    domain.remove(num)
            if box_y_index == 2:
                if count < 6 and num in domain:
                    domain.remove(num)
            else:
                domain.remove(num)
            count += 1


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
