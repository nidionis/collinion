from src.cell import Cell
import random

from src.kinds import Kinds


class Field:
    def __init__(self, kinds: Kinds, *size):
        self.width , self.height = size
        self.kinds = kinds
        self.cells = None
        self.cells = self.rand()
    
    def apply_rules(self, rules_fn):
        new_field = Field(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[y][x]
                new_kind = rules_fn(cell, self)
                if new_kind:
                    new_field.cells[y][x].kind = new_kind
                else:
                    new_field.cells[y][x].kind = cell.kind
        return new_field
    
    def count_neighbors(self, x, y, kind):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.cells[ny][nx].kind == kind:
                        count += 1
        return count
        
    def rand(self):
        self.cells = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Cell(self.kinds, x, y))
            self.cells.append(row)
