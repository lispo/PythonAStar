__author__ = 'Lispo'

from Node import *
from PathFinding import *

nodes = []

for i in range(40):
    for j in range(40):
        node = Node(GridPosition(i, j))
        nodes.append(node)

path_finding = PathFinding(39, 39, nodes)
path = path_finding.find_path(GridPosition(0, 0), GridPosition(2, 39))
print("DONE! \nYOUR PATH: ")

for i in range(len(path)):
    print(path[i].x, path[i].y)