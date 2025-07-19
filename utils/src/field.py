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
        inner_cells = self.cells[1:self.height-1, 1:self.width-1]
        it = np.nditer(inner_cells, flags=['refs_ok'])
        for cell in it:
            yield cell.item()

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
        y_coords, x_coords = np.mgrid[0:self.height, 0:self.width]
        
        for y in range(self.height):
            for x in range(self.width):
                border = self.is_border(y, x)
                if border:
                    self.set(borders[border], x, y)
                else:
                    self.set(self.kinds.rand(), x, y)
        return self

    def surround_field(self, up=None, down=None, left=None, right=None):
        x_indices = np.arange(self.width)
        for x in x_indices:
            self.set(up or borders["UP"], x, 0)
        for x in x_indices:
            self.set(down or borders["DOWN"], x, self.height-1)
        y_indices = np.arange(self.height)
        for y in y_indices:
            self.set(left or borders["LEFT"], 0, y)
        for y in y_indices:
            self.set(right or borders["RIGHT"], self.width-1, y)
            
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
            return "DOWN"
        return False
        
    def find_cells_by_kind(self, kind_name):
        if isinstance(kind_name, str):
            kind = self.kinds.kind(kind_name)
        else:
            kind = kind_name
            
        mask = np.zeros((self.height, self.width), dtype=bool)
        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[y, x]
                if cell is not None and cell.kind.name == kind.name:
                    mask[y, x] = True
        return np.where(mask)

    def neighbours(self, x, y):
        y_min = max(0, y-1)
        y_max = min(self.height, y+2)
        x_min = max(0, x-1)
        x_max = min(self.width, x+2)
        
        neighbors = self.cells[y_min:y_max, x_min:x_max].copy()
        # Calculate relative position of center cell
        rel_y, rel_x = y - y_min, x - x_min
        
        # Set center cell to None
        if (0 <= rel_y < neighbors.shape[0]) and (0 <= rel_x < neighbors.shape[1]):
            neighbors[rel_y, rel_x] = None
        return neighbors
