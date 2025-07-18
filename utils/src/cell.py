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
        return str(self.kind)

    def around(self, kind):
        count = 0
        neighbors = self.field.neighbours(self.x, self.y)
        for y in range(len(neighbors)):
            for x in range(len(neighbors[y])):
                if kind == neighbors[y][x]:
                    count += 1
        return count

    def side_up(self, kind):
        count = 0
        neighbors = self.field.neighbours(self.x, self.y)
        if self.y != 0:
            for cell in neighbors[0]:
                if kind == cell:
                    count += 1
        return count

    def side_down(self, kind):
        count = 0
        neighbors = self.field.neighbours(self.x, self.y)
        if self.y != len(neighbors) - 1:
            for cell in neighbors[-1]:
                if kind == cell:
                    count += 1
        return count

    def side_left(self, kind):
        count = 0
        neighbors = self.field.neighbours(self.x, self.y)
        if self.x != 0:
            for cell in neighbors[:, 0]:
                if kind == cell:
                    count += 1
        return count

    def side_right(self, kind):
        count = 0
        neighbors = self.field.neighbours(self.x, self.y)
        if self.x != len(neighbors[0]) - 1:
            for cell in neighbors[:, -1]:
                if kind == cell:
                    count += 1
        return count

    def up(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y-1][self.x]
        else:
            return self.field.cells[self.y-1][self.x]

    def down(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y+1][self.x]
        else:
            return self.field.cells[self.y+1][self.x]

    def right(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y][self.x+1]
        else:
            return self.field.cells[self.y][self.x+1]

    def left(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y][self.x-1]
        else:
            return self.field.cells[self.y][self.x-1]

    def up_right(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y-1][self.x+1]
        else:
            return self.field.cells[self.y-1][self.x+1]

    def up_left(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y-1][self.x-1]
        else:
            return self.field.cells[self.y-1][self.x-1]

    def down_right(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y+1][self.x+1]
        else:
            return self.field.cells[self.y+1][self.x+1]

    def down_left(self, kind=None):
        if kind:
            return kind == self.field.cells[self.y+1][self.x-1]
        else:
            return self.field.cells[self.y+1][self.x-1]
