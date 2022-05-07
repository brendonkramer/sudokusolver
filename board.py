#######################################################################################################################
# File: board.py
#
#######################################################################################################################

#imports
from numpy import *

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
          index = [row,col]
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
              count += (abs(this_row - goal_row) + abs(this_col - goal_col ))
            goal_col+=1
          goal_row+=1
        this_col+=1
      this_row+=1
    self._score = count + self.num_parents()

  def get_domain(self, x_index, y_index):
    domain_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
      if self._layout[x_index][i] != 0:
        domain_list.remove(self._layout[x_index][i])
    for i in range(9):
      if self._layout[i][y_index] != 0:
        domain_list.remove(self._layout[i][y_index])
    if x_index < 3 and y_index < 3:
      for i in range(3):
        for ii in range(3):
          if self._layout[i][ii] != 0:
            domain_list.remove(self._layout[i][ii])
    if 2 < x_index < 6 and y_index < 3:
      for i in range(3):
        for ii in range(3):
          if self._layout[i+3][ii] != 0:
            domain_list.remove(self._layout[i][ii])
    if x_index > 5 and y_index < 3:
      for i in range(3):
        for ii in range(3):
          if self._layout[i + 6][ii] != 0:
            domain_list.remove(self._layout[i][ii])
    if x_index < 3 and 2 < y_index < 6:
      for i in range(3):
        for ii in range(3):
          if self._layout[i][ii+3] != 0:
            domain_list.remove(self._layout[i][ii])
    if 2 < x_index < 6 and 2 < y_index < 6:
      for i in range(3):
        for ii in range(3):
          if self._layout[i + 3][ii + 3] != 0:
            domain_list.remove(self._layout[i][ii])
    if x_index > 5 and 2 < y_index < 6:
      for i in range(3):
        for ii in range(3):
          if self._layout[i + 6][ii + 3] != 0:
            domain_list.remove(self._layout[i][ii])
    if x_index < 3 and y_index > 5:
      for i in range(3):
        for ii in range(3):
          if self._layout[i][ii + 6] != 0:
            domain_list.remove(self._layout[i][ii])
    if 2 < x_index < 6 and y_index > 5:
      for i in range(3):
        for ii in range(3):
          if self._layout[i + 3][ii + 6] != 0:
            domain_list.remove(self._layout[i][ii])
    if x_index > 5 and y_index > 5:
      for i in range(3):
        for ii in range(3):
          if self._layout[i + 6][ii + 6] != 0:
            domain_list.remove(self._layout[i][ii])
    return domain_list



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
