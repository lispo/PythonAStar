__author__ = 'Lispo'

from GridPosition import *


class PathFinding():
    width = 0
    height = 0

    start_node = None
    end_node = None
    current_node = None

    close_list = []
    open_list = []
    nodes = []
    temp = []


    def __init__(self, width, height, nodes):
        self.width = width
        self.height = height
        self.nodes = nodes


    def find_path(self, start, end, unAvailables=None):
        for node in self.nodes:
            if unAvailables is not None and node.GridPosition in unAvailables:
                node.is_available = False
            else:
                node.is_available = True

            node.clear()
            del self.open_list[:]
            del self.close_list[:]

        self.start_node = self.get_node_by_grid_position(end)
        self.end_node = self.get_node_by_grid_position(start)

        self.start_node.is_available = self.end_node.is_available = True

        self.calculate_manhattan_cost(start)

        self.open_list.append(self.get_node_by_grid_position(end))
        self.temp.append(self.get_node_by_grid_position(end))
        self.current_node = self.get_node_by_grid_position(end)
        self.current_node.path_cost = 0
        self.current_node.result = self.current_node.path_cost + self.current_node.heuristic

        while self.current_node != self.end_node:
            self.get_neighbours(self.current_node)

            self.open_list.remove(self.current_node)
            self.close_list.append(self.current_node)

            if len(self.open_list) != 0:
                self.current_node = self.find_minimal_cell_cost()
            else:
                return self.create_path()

        self.open_list.remove(self.current_node)
        self.close_list.append(self.current_node)

        return self.create_path()

    def get_node_by_grid_position(self, grid_pos):
        for node in self.nodes:
            if node.grid_position.x == grid_pos.x and node.grid_position.y == grid_pos.y:
                return node

    def create_path(self):
        path = []
        curr_cell = self.close_list[len(self.close_list) - 1]

        while curr_cell is not self.start_node:
            curr_cell = curr_cell.parent
            if curr_cell is not None:
                path.append(curr_cell.grid_position)

        return path


    def find_minimal_cell_cost(self):
        cell = None
        for i in range(len(self.open_list)):
            if cell is None or cell.result > self.open_list[i].result:
                cell = self.open_list[i]
        return cell


    def get_neighbours(self, cell):
        self.add_neighbours(GridPosition.get_left(cell.grid_position), 10)
        self.add_neighbours(GridPosition.get_right(cell.grid_position), 10)
        self.add_neighbours(GridPosition.get_upper(cell.grid_position), 10)
        self.add_neighbours(GridPosition.get_lower(cell.grid_position), 10)
        self.add_neighbours(GridPosition.get_diagonel_left_top(cell.grid_position), 14)
        self.add_neighbours(GridPosition.get_diagonal_right_top(cell.grid_position), 14)
        self.add_neighbours(GridPosition.get_diagonal_left_bottom(cell.grid_position), 14)
        self.add_neighbours(GridPosition.get_diagonal_right_bottom(cell.grid_position), 14)

    def add_neighbours(self, position, path_cost):
        if not self.get_node_by_grid_position(position) or self.get_node_by_grid_position(position) in self.close_list or not \
                self.get_node_by_grid_position(position).is_available:
            return

        if not self.get_node_by_grid_position(position) in self.open_list:
            self.get_node_by_grid_position(position).parent = self.current_node
            self.get_node_by_grid_position(position).path_cost = self.current_node.path_cost + path_cost
            self.get_node_by_grid_position(position).result = self.get_node_by_grid_position(position).path_cost + self.get_node_by_grid_position(
                position).heuristic
            self.open_list.append(self.get_node_by_grid_position(position))

        else:
            if self.get_node_by_grid_position(position).path_cost > (
                        self.current_node.path_cost + self.get_path_cost(self.current_node.grid_position,
                                                                                self.get_node_by_grid_position(
                                                                                    position).grid_position)):
                self.get_node_by_grid_position(position).parent = self.current_node
                self.get_node_by_grid_position(position).path_cost = (
                    self.current_node.path_cost + self.get_path_cost(self.current_node.grid_position,
                                                                            self.get_node_by_grid_position(position).grid_position))
                self.get_node_by_grid_position(position).result = self.get_node_by_grid_position(position).path_cost + self.get_node_by_grid_position(
                    position).heuristic


    def calculate_manhattan_cost(self, end_point):
        for node in self.nodes:
            node.heuristic = (int)(
                abs(node.grid_position.x - end_point.x) + abs(node.grid_position.y - end_point.y)) * 10


    def get_path_cost(self, grid_position_from, grid_position_to):
        if grid_position_to.x > grid_position_from.x or grid_position_to.x < grid_position_from.x and grid_position_to.y > grid_position_from.y or grid_position_to.y < grid_position_from.y:
            return GridPosition.DIAGONAL_COST
        else:
            return GridPosition.ORTOGONAL_COST
