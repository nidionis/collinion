import pygame

from field import Field, borders
from kinds import Kinds
from display import Display
from cell import Cell

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
        self.next_field = None
        self.width = width
        self.height = height
        if not self.width:
            self.width = pygame.display.Info().current_w // self.zoom
        if not self.height:
            self.height = pygame.display.Info().current_h // self.zoom
        self.display = None
        self.reusable_cell = None

    def __iter__(self):
        return iter(self.field)

    def setup(self):
        if not self.field:
            self.field = Field(self.kinds, self.width, self.height)
            self.field.setup_kinds()
            self.field.rand()
        if not self.display:
            self.display = Display(self)
        return self

    def run(self):
        #self.setup()
        self.display.run()

    def add_kind(self, name, color, hotness=1, weight=1):
        self.kinds.add(name, color, hotness, weight)
        return self

    def randomize(self):
        if not self.field:
            self.field = Field(self.kinds, self.width, self.height)
        self.field.rand()
        return self

    def switch_cell(self, cell, rules):
        if not self.reusable_cell:
            self.reusable_cell = Cell(cell.kind, cell.x, cell.y, field=self.field)
        else:
            self.reusable_cell.update(cell, self.field)
            
        new_kind = str(rules(self.reusable_cell))
        try:
            kind_obj = self.kinds.kind(new_kind)
        except ValueError as e:
            if e.args[0] == "kind None not found":
                kind_obj = cell.kind
        self.next_field.set(kind_obj, cell.x, cell.y)

    def switch(self, rules):
        # Initialize the next field if not already done
        if self.next_field is None:
            self.next_field = Field(self.kinds, self.width, self.height)
        for cell in self:
            self.switch_cell(cell, rules)
        self.field, self.next_field = self.next_field, self.field
    
    def switch_all(self):
        for fts_rules in self.fts_rules:
            self.switch(fts_rules)
            yield  # Yield after each rule is applied

    def set_border(self, border, kind):
        borders[border] = kind
