import random

class CellType:
    _types = {}  # Class-level dictionary to store all cell types
    hotness_total = 0

    def __init__(self, name: str, color: str, hotness: float = 1):
        """
        Initialize a cell type with a name and color.
        :param name: Name of the cell type
        :param color: Color in hex format ("#RRGGBB")
        :param hotness: Hotness of the cell type (default: 1)
        """
        self.name = name
        self.color = color
        self.hotness = hotness
        # Store the type in the class-level dictionary
        CellType._types[name] = self
        CellType.hotness_total += hotness

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, CellType):
            return self.name == other.name
        return False

    def __sizeof__(self):
        return len(CellType._types)

    @classmethod
    def get(cls, name: str):
        """
        Retrieve a cell type by name.
        :param name: Name of the cell type
        :return: CellType instance
        :raises KeyError: If the cell type doesn't exist
        """
        if name not in cls._types:
            raise KeyError(f"Cell type '{name}' not found")
        return cls._types[name]

    @classmethod
    def gen_random(self):
        """
        Return a random cell type.
        Considering the hotness of each cell type,
        the probability of each type being chosen is proportional to its hotness.
        :return: CellType instance
        """
        # Check if any cell types exist
        if not self._types:
            raise ValueError("No cell types defined. Create cell types before generating random cells.")

        rand = random.random() * self.hotness_total
        cell_type = None  # Default value

        for type_instance in self._types.values():
            cell_type = type_instance  # Always keep the latest as fallback
            rand -= type_instance.hotness
            if rand <= 0:
                break

        # In case the loop didn't set cell_type (should not happen if hotness values are positive)
        if cell_type is None:
            return None
            #cell_type = next(iter(self._types.values()))

        cell = Cell(cell_type)
        return cell

class Cell:
    """
    Represents a cell with a specific type and position.
    """
    def __init__(self, cell_type: CellType, position: tuple = None):
        """
        Initialize a cell with a given type and optional position.
        :param cell_type: Type of the cell
        :param position: Optional tuple representing the cell's position (x, y)
        """
        self.type = cell_type
        self.position = position
        #self.x, self.y = position
        self.grid = None  # Reference to the grid will be set when added to a grid

    def __repr__(self):
        """
        String representation of the cell.
        :return: A string describing the cell's type
        """
        return self.type.name
        
    def __eq__(self, other):
        """
        Allow comparison between cells and strings/CellTypes.
        :param other: Another cell, cell type or string to compare
        :return: Boolean indicating equality
        """
        if isinstance(other, str):
            return self.type.name == other
        elif isinstance(other, CellType):
            return self.type.name == other.name
        elif isinstance(other, Cell):
            return self.type.name == other.type.name
        return False

    def update(self, new_type: CellType):
        """
        Update the cell's type.
        :param new_type: New CellType for the cell
        """
        self.type = new_type
        
    def around(self, cell_type):
        """
        Check if there are neighboring cells of a specific type.
        :param cell_type: CellType or string to check for
        :return: List of neighboring cells of the specified type
        """
        if self.grid is None:
            return []

        # Get position
        x, y = self.position

        # Define possible neighboring positions
        neighbors = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]

        # Filter and return neighbors matching the specified type
        matching_neighbors = []
        for nx, ny in neighbors:
            if 0 <= nx < self.grid.width and 0 <= ny < self.grid.height:
                neighbor_cell = self.grid.get_cell(nx, ny)
                if isinstance(cell_type, str):
                    if neighbor_cell.type.name == cell_type:
                        matching_neighbors.append(neighbor_cell)
                elif isinstance(cell_type, CellType):
                    if neighbor_cell.type.name == cell_type.name:
                        matching_neighbors.append(neighbor_cell)
        return len(matching_neighbors)

    def x(self):
        return self.position[0]
    def y(self):
        return self.position[1]