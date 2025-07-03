from src.cell import Cell
import random
from src.kinds import Kinds, Kind
import numpy as np


class Field:
    def __init__(self, kinds: Kinds, *size):
        self.width , self.height = size
        self.kinds = kinds
        self.cells = np.empty((self.height, self.width), dtype=object)
        self.cells_tmp = np.empty((self.height, self.width), dtype=object)

    def apply_rules(self, rules_fn):
        ## Create a new temporary array and apply rules vectorized
        #self.cells_tmp = np.empty((self.height, self.width), dtype=object)

        # Prepare arrays for vectorized operations
        y_coords, x_coords = np.mgrid[0:self.height, 0:self.width]

        # Vectorized rule application
        for y, x in np.nditer([y_coords, x_coords]):
            cell = self.cells[y, x]
            try:
                new_kind = rules_fn(cell, self)
                kind_obj = self.kinds.kind(new_kind)
                self.cells_tmp[y, x] = Cell(kind_obj, x, y)
            except ValueError as e:
                print(f"Warning: {e}, keeping original kind for cell at ({x}, {y})")
                self.cells_tmp[y, x] = cell

        # Swap buffers
        self.cells, self.cells_tmp = self.cells_tmp, self.cells
        return self
    
    def count_neighbors(self, x, y, kind):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if str(self.cells[ny][nx].kind) == kind:
                        count += 1
        return count
        
    def rand(self):
        self.cells = np.empty((self.height, self.width), dtype=object)
        for y in range(self.height):
            for x in range(self.width):
                random_kind = self.kinds.rand()
                self.cells[y][x] = Cell(random_kind, x, y)
        return self
