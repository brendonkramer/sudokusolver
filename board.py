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
  def __init__(self, layout,score=None):
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

  def get_domain(self, x_index, y_index):
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
          if self._layout[y, x+3] != 0:
            if self._layout[y, x+3] in domain_list:
              domain_list.remove(self._layout[y, x+3])
    if x_index > 5 and y_index < 3:
      for y in range(3):
        for x in range(3):
          if self._layout[y, x+6] != 0:
            if self._layout[y, x+6] in domain_list:
              domain_list.remove(self._layout[y, x+6])
    if x_index < 3 and 2 < y_index < 6:
      for y in range(3):
        for x in range(3):
          if self._layout[y+3, x] != 0:
            if self._layout[y+3, x] in domain_list:
              domain_list.remove(self._layout[y+3, x])
    if 2 < x_index < 6 and 2 < y_index < 6:
      for y in range(3):
        for x in range(3):
          if self._layout[y + 3, x + 3] != 0:
            if self._layout[y+3, x+3] in domain_list:
              domain_list.remove(self._layout[y+3, x+3])
    if x_index > 5 and 2 < y_index < 6:
      for y in range(3):
        for x in range(3):
          if self._layout[y + 3,x + 6] != 0:
            if self._layout[y+3, x+6] in domain_list:
              domain_list.remove(self._layout[y+3, x+6])
    if x_index < 3 and y_index > 5:
      for y in range(3):
        for x in range(3):
          if self._layout[y+6,x] != 0:
            if self._layout[y+6, x] in domain_list:
              domain_list.remove(self._layout[y+6, x])
    if 2 < x_index < 6 and y_index > 5:
      for y in range(3):
        for x in range(3):
          if self._layout[y + 6,x + 3] != 0:
            if self._layout[y+6, x+3] in domain_list:
              domain_list.remove(self._layout[y+6, x+3])
    if x_index > 5 and y_index > 5:
      for y in range(3):
        for x in range(3):
          if self._layout[y + 6,x + 6] != 0:
            if self._layout[y+6, x+6] in domain_list:
              domain_list.remove(self._layout[y+6, x+6])
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
