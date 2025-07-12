import pygame

from field import Field
from kinds import Kinds
from display import Display
from cell import CellProxy, Cell
from rules import setup, rules

class Game:
    FIELD_WIDTH = 100
    FIELD_HEIGHT = 150
    """Game class that manages the cellular automaton simulation"""
    def __init__(self, zoom=500):
        pygame.init()
        self.zoom = zoom
        self.kinds = Kinds()
        self.field = None
        self.width = self.FIELD_WIDTH
        self.height = self.FIELD_HEIGHT
        self.display = None
        
    def setup(self):
        """Initialize the field with the registered kinds"""
        if not self.field:
            self.field = Field(self.kinds, self.width, self.height)
            self.field.rand()
        if not self.display:
            self.display = Display(self)
        return self
        
    def add_kind(self, name, color, hotness=1):
        """Register a new cell kind"""
        self.kinds.add(name, color, hotness)
        return self
        
    def randomize(self):
        """Fill the field with random cell kinds"""
        if not self.field:
            self.field = Field(self.kinds, self.width, self.height)
        self.field.rand()
        return self
        
    def run(self, rules):
        """Start the simulation with the given rules"""
        self.setup()
        self.display.run(rules)

    def switch_cell(self, cell, rules):
        cell_proxy = CellProxy(cell, self.field)
        return str(rules(cell_proxy))

    def switch(self, rules):
        new_cells = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                cell = self.field.cells[y][x]
                new_kind = str(self.switch_cell(cell, rules))
                if not new_kind:
                    new_kind = str(cell)
                kind_obj = self.kinds.kind(new_kind)
                row.append(Cell(kind_obj, x, y))
            new_cells.append(row)
        self.field.cells = new_cells
        #return new_cells