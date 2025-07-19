from itertools import count
import numpy as np

from kinds import Kinds, Kind

class Cell:
    def __init__(self, kind: Kind, *pos):
        self.x, self.y = pos
        self.kind = kind

    def __str__(self):
        return str(self.kind)

    def __repr__(self):
        return self.kind

    def __eq__(self, other):
        return str(self) == str(other)

    def rgb(self):
        return Kinds.rgb(self.kind)

class CellProxy:
    def __init__(self, cell, field):
        self.cell = cell
        self.field = field
        self.x = cell.x
        self.y = cell.y
        self.kind = cell.kind

    def __eq__(self, other):
        return str(self.cell) == str(other)

    def __str__(self):
        return str(self.kind)

    def __repr__(self):
        return str(self.kind)

    def around(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        # More efficient counting using vectorized operation
        count = sum(1 for cell in neighbors.flat if cell is not None and kind == cell)
        return count

    def side_up(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        if self.y != 0 and neighbors.shape[0] > 0:
            # Count matching cells in the top row
            return sum(1 for cell in neighbors[0] if cell is not None and kind == cell)
        return 0

    def side_down(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        if neighbors.shape[0] > 0:
            # Count matching cells in the bottom row
            return sum(1 for cell in neighbors[-1] if cell is not None and kind == cell)
        return 0

    def side_left(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        if neighbors.shape[1] > 0:
            # Count matching cells in the leftmost column
            return sum(1 for cell in neighbors[:, 0] if cell is not None and kind == cell)
        return 0

    def side_right(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        if neighbors.shape[1] > 0:
            # Count matching cells in the rightmost column
            return sum(1 for cell in neighbors[:, -1] if cell is not None and kind == cell)
        return 0

    def up(self, kind=None):
        # NumPy array indexing
        if kind:
            return kind == self.field.cells[self.y-1, self.x]
        else:
            return self.field.cells[self.y-1, self.x]

    def down(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y+1, self.x]
        else:
            return self.field.cells[self.y+1, self.x]

    def right(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y, self.x+1]
        else:
            return self.field.cells[self.y, self.x+1]

    def left(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y, self.x-1]
        else:
            return self.field.cells[self.y, self.x-1]

    def up_right(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y-1, self.x+1]
        else:
            return self.field.cells[self.y-1, self.x+1]

    def up_left(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y-1, self.x-1]
        else:
            return self.field.cells[self.y-1, self.x-1]

    def down_right(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y+1, self.x+1]
        else:
            return self.field.cells[self.y+1, self.x+1]

    def down_left(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y+1, self.x-1]
        else:
            return self.field.cells[self.y+1, self.x-1]
