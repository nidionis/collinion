import pygame

from field import Field
from kinds import Kinds
from display import Display
from cell import CellProxy, Cell

import importlib
import inspect



class Game:

    def __init__(self, width=None, height=None, zoom=10, f_rules="rules"):
        pygame.init()
        self.kinds = Kinds()

        mod = importlib.import_module(f_rules)
        self.fts_rules = [
            obj
            for name, obj in inspect.getmembers(mod, inspect.isfunction)
            if not "__" in name and name != "setup"
        ]

        self.zoom = zoom # default nb pixels per cell
        self.field = None
        self.width = width
        self.height = height
        if not self.width:
            self.width = pygame.display.Info().current_w // self.zoom
        if not self.height:
            self.height = pygame.display.Info().current_h // self.zoom
        self.display = None

    def setup(self):
        if not self.field:
            self.field = Field(self.kinds, self.width, self.height)
            self.field.rand()
        if not self.display:
            self.display = Display(self)
        return self

    def run(self):
        #self.setup()
        self.display.run()

    def add_kind(self, name, color, hotness=1):
        self.kinds.add(name, color, hotness)
        return self
        
    def randomize(self):
        if not self.field:
            self.field = Field(self.kinds, self.width, self.height)
        self.field.rand()
        return self

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

    def switch_all(self):
        for fts_rules in self.fts_rules:
            self.switch(fts_rules)