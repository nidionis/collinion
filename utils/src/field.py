from cell import Cell
import random
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
        self.width , self.height = size
        self.kinds = kinds
        self.setup_kinds()
        self.cells = [ [ 0 for x in range(size[0]) ] for y in range(size[1]) ]
        #self.surround_field()
        self.rand()

    def __iter__(self):
        for y in range(1, self.height - 1):  # rows inside the border
            for x in range(1, self.width - 1):  # columns inside the border
                yield self.cells[y][x]  # or: yield sel

    def __copy__(self):
        cpy = Field(self.kinds, self.width, self.height)

    def set(self, kind, x, y):
        if isinstance(kind, str):
            kind = self.kinds.kind(kind)
        cell = Cell(kind, x, y)
        self.cells[y][x] = cell

    def rand(self):
        for y in range(self.height):
            for x in range(self.width):
                border = self.is_border(y, x)
                if border:
                    self.set(borders[border], x, y)
                else:
                    self.set(self.kinds.rand(), x, y)

    def surround_field(self, up=None, down=None, left=None, right=None):
        for y in range(self.height):
            for x in range(self.width):
                for y in range(self.height):
                    for x in range(self.width):
                        if y == 0:
                            self.set(borders["UP"], x, y)
                        if y == self.height - 1:
                            self.set(borders["DOWN"], x, y)
                        if x == 0:
                            self.set(borders["LEFT"], x, y)
                        if x == self.width - 1:
                            self.set(borders["RIGHT"], x, y)
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
        ls_neighbours = []
        for i_y in range(y-1, y+2):
            row = []
            for i_x in range(x-1, x+2):
                if not self.is_border(i_y, i_x):
                    if i_x == x and i_y == y:
                        row.append(None)
                    else:
                        row.append(self.cells[i_y][i_x])
            ls_neighbours.append(row)
        return ls_neighbours
