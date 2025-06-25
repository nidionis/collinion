from classes.Cell import Cell, CellType

class Grid:
    def __init__(self, cell_types: CellType, width: int = 640, height: int = 480):
        self.width = width
        self.height = height
        self.cell_types = cell_types
        self.cells = []

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
#    def display(self):
#        for row in self.cells:
#            for cell in row:
#                cell.display()
#            print()