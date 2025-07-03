from src.field import Field
from src.kinds import Kinds
from src.display import Display

class CellProxy:
    """A proxy object that wraps a Cell and adds context about the field"""
    def __init__(self, cell, field):
        self.cell = cell
        self.field = field
        self.x = cell.x
        self.y = cell.y
        self.kind = str(cell.kind)  # Store the kind as string for easier comparison

    def __eq__(self, other):
        """Allow direct comparison with strings"""
        if isinstance(other, str):
            return self.kind == other
        return str(self.cell) == str(other)

    def __str__(self):
        return self.kind

    def __repr__(self):
        return self.kind

    def around(self, kind_name):
        """Count neighbors of a specific kind"""
        return self.field.count_neighbors(self.x, self.y, kind_name)

class Game:
    """Game class that manages the cellular automaton simulation"""
    
    def __init__(self, width=100, height=100):
        self.kinds = Kinds()
        self.field = None
        self.width = width
        self.height = height
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