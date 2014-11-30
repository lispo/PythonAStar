__author__ = 'Lispo'


class Node():
    heuristic = 0
    path_cost = 0
    result = 0
    parent = None
    grid_position = None
    is_available = False

    def __init__(self, grid_position):
        self.grid_position = grid_position

    def clear(self):
        self.heuristic = self.pathCost = self.result = 0
        self.parent = None