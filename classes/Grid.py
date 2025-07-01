from classes.Cell import Cell, CellType
from classes.display import display_game
from copy import deepcopy

class Grid:
    def __init__(self, cell_types: CellType, width: int = 640, height: int = 480, scale: int = 10):
        self.width = width
        self.height = height
        self.scale = scale
        self.cell_types = cell_types
        self.cells = []
        self.display_ =  display_game(self, width=width * scale, height=height * scale, title="Collinion")

    def __deepcopy__(self, memo):
        # if we’ve already copied this instance, return it
        if id(self) in memo:
            return memo[id(self)]

        # 1) make a bare instance without running __init__
        cls = self.__class__
        new = cls.__new__(cls)
        memo[id(self)] = new

        # 2) copy primitive attributes by hand
        new.cell_types = self.cell_types  # probably immutable or shared
        new.width = self.width
        new.height = self.height

        # 3) deep‐copy the cell matrix
        new.cells = [
            [deepcopy(cell, memo) for cell in row]
            for row in self.cells
        ]

        # why this way block the window ?
        new.display_ = self.display_

        return new

    def get_cell(self, x: int, y: int) -> Cell:
        """
        Get the cell at the specified coordinates.
        :param x: X coordinate
        :param y: Y coordinate
        :return: Cell at the specified position
        :raises IndexError: If coordinates are out of bounds
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        raise IndexError(f"Cell coordinates ({x}, {y}) out of bounds")

    def set_cell(self, x: int, y: int, cell_type: CellType) -> Cell:
        """
        Set the cell type at the specified coordinates.
        :param x: X coordinate
        :param y: Y coordinate
        :param cell_type: CellType to set
        :return: Updated cell
        :raises IndexError: If coordinates are out of bounds
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.cells[y][x].update(cell_type)
            return self.cells[y][x]
        #raise IndexError(f"Cell coordinates ({x}, {y}) out of bounds")

    def create_random_grid(self):
        # Initialize the grid with default cells
        for y in range(self.height):
            row = []
            for x in range(self.width):
                cell = self.cell_types.gen_random()
                cell.grid = self  # Set reference to this grid
                cell.position = (x, y)
                row.append(cell)
            self.cells.append(row)

    def display_frame(self):
        self.display_.display_grid()