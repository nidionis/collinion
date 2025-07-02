from src.cell import Cell
import random

class Matrix:
    def __init__(self, width, height, kind=None):
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y, kind) for x in range(width)] for y in range(height)]
    
    def apply_rules(self, rules_fn):
        new_matrix = Matrix(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[y][x]
                new_kind = rules_fn(cell, self)
                if new_kind:
                    new_matrix.cells[y][x].kind = new_kind
                else:
                    new_matrix.cells[y][x].kind = cell.kind
        return new_matrix
    
    def count_neighbors(self, x, y, kind):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.cells[ny][nx].kind == kind:
                        count += 1
        return count
        
    def randomize(self, Kinds, fill_ratio=1.0):
        """
        Randomize the matrix cells based on cell kind hotness values.
        
        :param Kinds: The registry containing cell Kinds and hotness values
        :param fill_ratio: The percentage of cells to randomize (0.0-1.0)
        """
        # Get all cells as a flat list
        all_cells = []
        for y in range(self.height):
            for x in range(self.width):
                kind = Kinds.rand()
                all_cells[y].append()

        # Calculate number of cells to fill
        num_to_fill = int(len(all_cells) * fill_ratio)
        
        # Randomly select cells to fill
        cells_to_fill = random.sample(all_cells, num_to_fill)
        
        # Set random kind based on hotness
        for x, y in cells_to_fill:
            kind = Kinds.rand()
            self.cells[y][x].kind = kind
