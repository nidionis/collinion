from itertools import count
import numpy as np

from kinds import Kinds, Kind

class Cell:
    def __init__(self, kind: Kind, *pos, field=None):
        self.x, self.y = pos
        self.kind = kind
        self.field = field
        self.cache = {}  # Add cache for performance

    def __str__(self):
        return str(self.kind)

    def __repr__(self):
        return str(self.kind)

    def __eq__(self, other):
        if str(self) == str(other):
            return True

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __gt__(self, other):
        return self.weight() > other.weight()

    def __le__(self, other):
        return self.weight() <= other.weight()

    def __ge__(self, other):
        return self.weight() >= other.weight()

    def update(self, cell=None, field=None):
        """Update this cell's properties from another cell without creating a new object"""
        if cell:
            self.x = cell.x
            self.y = cell.y
            self.kind = cell.kind
        if field is not None:
            self.field = field
        # Clear cache as properties have changed
        self.cache = {}
        return self

    def rgb(self):
        return Kinds.rgb(self.kind)

    def around(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        count = sum(1 for cell in neighbors.flat if cell is not None and kind == cell)
        return count

    def side_up(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        if self.y != 0 and neighbors.shape[0] > 0:
            return sum(1 for cell in neighbors[0] if cell is not None and kind == cell)
        return 0

    def side_down(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        if neighbors.shape[0] > 0:
            return sum(1 for cell in neighbors[-1] if cell is not None and kind == cell)
        return 0

    def side_left(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        if neighbors.shape[1] > 0:
            return sum(1 for cell in neighbors[:, 0] if cell is not None and kind == cell)
        return 0

    def side_right(self, kind):
        neighbors = self.field.neighbours(self.x, self.y)
        if neighbors.shape[1] > 0:
            return sum(1 for cell in neighbors[:, -1] if cell is not None and kind == cell)
        return 0

    def up(self, kind=None):
        try:
            if kind:
                return kind == self.field.cells[self.y-1, self.x]
            else:
                return self.field.cells[self.y-1, self.x]
        except (IndexError, AttributeError):
            return None if kind is None else False

    def down(self, kind=None):
        try:
            if kind:
                return kind == self.field.cells[self.y+1, self.x]
            else:
                return self.field.cells[self.y+1, self.x]
        except (IndexError, AttributeError):
            return None if kind is None else False

    def right(self, kind=None):
        try:
            if kind:
                return kind == self.field.cells[self.y, self.x+1]
            else:
                return self.field.cells[self.y, self.x+1]
        except (IndexError, AttributeError):
            return None if kind is None else False

    def left(self, kind=None):
        try:
            if kind:
                return kind == self.field.cells[self.y, self.x-1]
            else:
                return self.field.cells[self.y, self.x-1]
        except (IndexError, AttributeError):
            return None if kind is None else False

    def up_right(self, kind=None):
        try:
            if kind:
                return kind == self.field.cells[self.y-1, self.x+1]
            else:
                return self.field.cells[self.y-1, self.x+1]
        except (IndexError, AttributeError):
            return None if kind is None else False

    def up_left(self, kind=None):
        try:
            if kind:
                return kind == self.field.cells[self.y-1, self.x-1]
            else:
                return self.field.cells[self.y-1, self.x-1]
        except (IndexError, AttributeError):
            return None if kind is None else False

    def down_right(self, kind=None):
        try:
            if kind:
                return kind == self.field.cells[self.y+1, self.x+1]
            else:
                return self.field.cells[self.y+1, self.x+1]
        except (IndexError, AttributeError):
            return None if kind is None else False

    def down_left(self, kind=None):
        try:
            if kind:
                return kind == self.field.cells[self.y+1, self.x-1]
            else:
                return self.field.cells[self.y+1, self.x-1]
        except (IndexError, AttributeError):
            return None if kind is None else False

    def weight(self):
        return self.kind.weight
