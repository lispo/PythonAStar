__author__ = 'Lispo'


class GridPosition():
    SHIFT = 1
    DIAGONAL_COST = 14
    ORTOGONAL_COST = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(start, end):
        return abs(start.x - end.x) + abs(start.y - end.y)

    @staticmethod
    def get_left(grid_position):
        return GridPosition(grid_position.x - GridPosition.SHIFT, grid_position.y)

    @staticmethod
    def get_right(grid_position):
        return GridPosition(grid_position.x + GridPosition.SHIFT, grid_position.y)

    @staticmethod
    def get_upper(grid_position):
        return GridPosition(grid_position.x, grid_position.y - GridPosition.SHIFT)

    @staticmethod
    def get_lower(grid_position):
        return GridPosition(grid_position.x, grid_position.y + GridPosition.SHIFT)

    @staticmethod
    def get_diagonel_left_top(grid_position):
        return GridPosition(grid_position.x - GridPosition.SHIFT, grid_position.y - GridPosition.SHIFT)

    @staticmethod
    def get_diagonal_right_top(grid_position):
        return GridPosition(grid_position.x + GridPosition.SHIFT, grid_position.y - GridPosition.SHIFT)

    @staticmethod
    def get_diagonal_left_bottom(grid_position):
        return GridPosition(grid_position.x - GridPosition.SHIFT, grid_position.y + GridPosition.SHIFT)

    @staticmethod
    def get_diagonal_right_bottom(grid_position):
        return GridPosition(grid_position.x + GridPosition.SHIFT, grid_position.y + GridPosition.SHIFT)

    @staticmethod
    def get_path_cost(grid_position_from, grid_position_to):
        if grid_position_to.x > grid_position_from.x or grid_position_to.x < grid_position_from.x & grid_position_to.y > grid_position_from.y or grid_position_to.y < grid_position_from.y:
            return GridPosition.DIAGONAL_COST
        else:
            return GridPosition.ORTOGONAL_COST

