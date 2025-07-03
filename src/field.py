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
        # Create a new temporary array for the next generation
        self.cells_tmp = np.empty((self.height, self.width), dtype=object)
        
        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[y][x]
                try:
                    new_kind = rules_fn(cell, self)
                    
                    # Create a new cell with the new kind
                    kind_obj = self.kinds.kind(new_kind)
                    new_cell = Cell(kind_obj, x, y)
                    self.cells_tmp[y][x] = new_cell
                except ValueError as e:
                    # If kind not found, keep the old kind
                    print(f"Warning: {e}, keeping original kind for cell at ({x}, {y})")
                    self.cells_tmp[y][x] = cell
                
        # Swap the arrays
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
