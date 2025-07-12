import pygame

from field import Field
from kinds import Kinds
from display import Display
from cell import CellProxy, Cell
from rules import setup, rules

class Game:
    """Game class that manages the cellular automaton simulation"""
    def __init__(self, width=None, height=None, zoom=10):
        pygame.init()
        self.zoom = zoom # default nb pixels per cell
        self.kinds = Kinds()
        self.field = None
        self.width = width
        self.height = height
        if not self.width:
            self.width = pygame.display.Info().current_w // self.zoom
        if not self.height:
            self.height = pygame.display.Info().current_h // self.zoom
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
                new_kind = self.switch_cell(cell, rules)
                try:
                    kind_obj = self.kinds.kind(new_kind)
                except ValueError as e:
                    if e.args[0] == "kind None not found":
                        kind_obj = cell.kind
                row.append(Cell(kind_obj, x, y))
            new_cells.append(row)
        self.field.cells = new_cells
        #return new_cells