from cell import Cell
import random
import numpy as np
from kinds import Kinds, Kind

global borders
borders = {
    "UP": "UP",
    "DOWN": "DOWN",
    "LEFT": "LEFT",
    "RIGHT": "RIGHT",
}

class Field:
    def __init__(self, kinds: Kinds, *size):
        self.width, self.height = size
        self.kinds = kinds
        self.setup_kinds()
        # Use NumPy array instead of nested lists
        self.cells = np.empty((self.height, self.width), dtype=object)
        self.rand()

    def __iter__(self):
        # Use flat indexing for better performance
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                yield self.cells[y, x]

    def __copy__(self):
        cpy = Field(self.kinds, self.width, self.height)
        cpy.cells = self.cells.copy()
        return cpy

    def set(self, kind, x, y):
        if isinstance(kind, str):
            kind = self.kinds.kind(kind)
        cell = Cell(kind, x, y)
        self.cells[y, x] = cell

    def rand(self):
        border_mask = np.zeros((self.height, self.width), dtype=bool)
        border_mask[0, :] = True
        border_mask[-1, :] = True
        border_mask[:, 0] = True
        border_mask[:, -1] = True
        
        for y in range(self.height):
            for x in range(self.width):
                border = self.is_border(y, x)
                if border:
                    self.set(borders[border], x, y)
                else:
                    self.set(self.kinds.rand(), x, y)

    def surround_field(self, up=None, down=None, left=None, right=None):
        for x in range(self.width):
            self.set(borders["UP"], x, 0)
        for x in range(self.width):
            self.set(borders["DOWN"], x, self.height-1)
        for y in range(self.height):
            self.set(borders["LEFT"], 0, y)
        for y in range(self.height):
            self.set(borders["RIGHT"], self.width-1, y)
            
        return self

    def setup_kinds(self):
        self.kinds.add("UP", "black", hotness=0)
        self.kinds.add("DOWN", "black", hotness=0)
        self.kinds.add("RIGHT", "black", hotness=0)
        self.kinds.add("LEFT", "black", hotness=0)

    def set_border(self, border, kind):
        borders[border] = kind

    def is_border(self, y, x):
        if x <= 0:
            return "LEFT"
        if x >= self.width - 1:
            return "RIGHT"
        if y <= 0:
            return "UP"
        if y >= self.height - 1:
            return "RIGHT"
        return False

    def neighbours(self, x, y):
        y_min = max(0, y-1)
        y_max = min(self.height, y+2)
        x_min = max(0, x-1)
        x_max = min(self.width, x+2)
        
        neighbors = np.empty((y_max-y_min, x_max-x_min), dtype=object)
        
        for i, i_y in enumerate(range(y_min, y_max)):
            for j, i_x in enumerate(range(x_min, x_max)):
                if i_x == x and i_y == y:
                    neighbors[i, j] = None
                else:
                    neighbors[i, j] = self.cells[i_y, i_x]
        return neighbors
