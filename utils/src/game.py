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
        self.setup_kinds()

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

    def __iter__(self):
        return iter(self.field)

    def setup_kinds(self):
        self.kinds = Kinds()
        self.add_kind("UP", "black", hotness=0)
        self.add_kind("DOWN", "black", hotness=0)
        self.add_kind("RIGHT", "black", hotness=0)
        self.add_kind("LEFT", "black", hotness=0)
        self.borders = {
            "UP": self.kinds.kind("UP"),
            "DOWN": self.kinds.kind("DOWN"),
            "LEFT": self.kinds.kind("LEFT"),
            "RIGHT": self.kinds.kind("RIGHT")
        }

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

    def set_border(self, border, kind):
        self.borders[border] = self.kinds.kind(kind)

    def set_borders(self, up=None, down=None, left=None, right=None):
        if up:
            self.set_border("UP", up)
        if down:
            self.set_border("DOWN", down)
        if left:
            self.set_border("LEFT", left)
        if right:
            self.set_border("RIGHT", right)

    def randomize(self):
        if not self.field:
            self.field = Field(self.kinds, self.width, self.height)
        self.field.rand()
        return self

    def switch_cell(self, cell, rules):
        cell_proxy = CellProxy(cell, self.field)
        new_kind = str(rules(cell_proxy))
        try:
            kind_obj = self.kinds.kind(new_kind)
        except ValueError as e:
            if e.args[0] == "kind None not found":
                kind_obj = cell.kind
        self.next_field.set(Cell(kind_obj, cell.x, cell.y), cell.x, cell.y)

    def switch(self, rules):
        self.next_field = Field(self.kinds, self.width, self.height)
        for cell in self:
            self.switch_cell(cell, rules)
        self.field = self.next_field

    def switch_all(self):
        for fts_rules in self.fts_rules:
            self.switch(fts_rules)