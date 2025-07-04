import pygame

from field import Field
from kinds import Kinds
from display import Display
from cell import CellProxy

class Game:
    """Game class that manages the cellular automaton simulation"""
    def __init__(self, zoom=10):
        pygame.init()
        self.zoom = zoom
        self.kinds = Kinds()
        self.field = None
        self.width = pygame.display.Info().current_w // self.zoom
        self.height = pygame.display.Info().current_h // self.zoom
        self.display = None
        
    def setup(self):
        """Initialize the field with the registered kinds"""
        if not self.field:
            self.field = Field(self.kinds, self.width, self.height)
            self.field.rand()
        if not self.display:
            self.display = Display(self.field, self.kinds)
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
        
    def run(self, rules_function):
        """Start the simulation with the given rules"""
        self.setup()
            
        # Create a wrapper for the rules function that provides CellProxy objects
        def rules_wrapper(cell, field):
            cell_proxy = CellProxy(cell, field)
            result = rules_function(cell_proxy)
            
            # Handle different return types
            if isinstance(result, str):
                return result
            elif isinstance(result, CellProxy):
                return result.kind
            else:
                return str(cell.kind)
                
        self.display.run(rules_wrapper)
        
    def turn(self, rules_function):
        """Apply one generation of rules and return the game object"""
        self.setup()
            
        # Create a wrapper as above
        def rules_wrapper(cell, field):
            cell_proxy = CellProxy(cell, field)
            result = rules_function(cell_proxy)
            
            # Handle different return types
            if isinstance(result, str):
                return result
            elif isinstance(result, CellProxy):
                return result.kind
            else:
                return str(cell.kind)
                
        self.field.apply_rules(rules_wrapper)
        return self