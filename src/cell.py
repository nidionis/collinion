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
        self.kind = str(cell.kind)  # Store the kind as string for easier comparison

    def __eq__(self, other):
        if isinstance(other, str):
            return self.kind == other
        return str(self.cell) == str(other)

    def __str__(self):
        return self.kind

    def __repr__(self):
        return self.kind

    def around(self, kind_name):
        """Count neighbors of a specific kind"""
        #return self.field.count_neighbors(self.x, self.y, kind_name)
        count = 0
        neighbors = self.field.neighbours(self.x, self.y)
        # renvoit une grille de 3 * 3 (si carre)
        for y in range(len(neighbors)):
            for x in range(len(neighbors[y])):
                if x or y:
                    if kind_name == str(neighbors[y][x]):
                        count += 1
        return count


