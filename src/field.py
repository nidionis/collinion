from cell import Cell
import random
from kinds import Kinds, Kind
import numpy as np

class Field:
    def __init__(self, kinds: Kinds, *size):
        self.width , self.height = size
        self.kinds = kinds
        self.cells = np.empty((self.height, self.width), dtype=object)

    def apply_rules(self, rules_fn):
        cells_tmp = np.empty((self.height, self.width), dtype=object)
        # Prepare arrays for vectorized operations
        y_coords, x_coords = np.mgrid[0:self.height, 0:self.width]
        # Vectorized rule application
        for y, x in np.nditer([y_coords, x_coords]):
            cell = self.cells[y, x]
            new_kind = rules_fn(cell, self)
            kind_obj = self.kinds.kind(new_kind)
            cells_tmp[y, x] = Cell(kind_obj, x, y)
        self.cells = cells_tmp
        return self

    def rand(self):
        self.cells = np.empty((self.height, self.width), dtype=object)
        for y in range(self.height):
            for x in range(self.width):
                random_kind = self.kinds.rand()
                self.cells[y][x] = Cell(random_kind, x, y)
        return self

    def is_border(self, y, x):
        if x <= 0 or x >= self.width - 1:
            return True
        if y <= 0 or y >= self.height - 1:
            return True
        return False

    def neighbours(self, x, y):
        # return the 3x3 grid of cells around (x, y) (including itself)
        neighbours = []
        for y in range(y-1, y+2):
            row = []
            for x in range(x-1, x+2):
                if not self.is_border(y, x):
                    row.append(self.cells[y][x])
            neighbours.append(row)
        return neighbours
