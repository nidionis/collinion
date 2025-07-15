from cell import Cell
import random
from kinds import Kinds, Kind

class Field:
    def __init__(self, kinds: Kinds, *size):
        self.width , self.height = size
        self.kinds = kinds
        self.cells = []
        self.init()

    def __iter__(self):
        for y in range(1, self.height - 1):  # rows inside the border
            for x in range(1, self.width - 1):  # columns inside the border
                yield self.cells[y][x]  # or: yield sel

    def init(self, map=None):
        self.rand()

    def set(self, kind, x, y):
        self.cells[y][x] = kind

    def rand(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                random_kind = self.kinds.rand()
                row.append(Cell(random_kind, x, y))
            self.cells.append(row)
        return self

    def is_border(self, y, x):
        if x <= 0 or x >= self.width - 1:
            return True
        if y <= 0 or y >= self.height - 1:
            return True
        return False

    def neighbours(self, x, y):
        ls_neighbours = []
        for i_y in range(y-1, y+2):
            row = []
            for i_x in range(x-1, x+2):
                if not self.is_border(i_y, i_x):
                    if i_x == x and i_y == y:
                        row.append(None)
                    else:
                        row.append(self.cells[i_y][i_x])
            ls_neighbours.append(row)
        return ls_neighbours
