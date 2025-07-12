from itertools import count

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
        return self.kind

    def around(self, kind):
        """Count neighbors of a specific kind"""
        count = 0
        neighbors = self.field.neighbours(self.x, self.y)
        for y in range(len(neighbors)):
            for x in range(len(neighbors[y])):
                if kind == neighbors[y][x]:
                    count += 1
        return count


