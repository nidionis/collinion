from cell_matrix.cell import Cell
import random

class Matrix:
    def __init__(self, width, height, default_type="empty"):
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y, default_type) for x in range(width)] for y in range(height)]
    
    def apply_rules(self, rules_fn):
        new_matrix = Matrix(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[y][x]
                new_type = rules_fn(cell, self)
                if new_type:
                    new_matrix.cells[y][x].type = new_type
                else:
                    new_matrix.cells[y][x].type = cell.type
        return new_matrix
    
    def count_neighbors(self, x, y, cell_type):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.cells[ny][nx].type == cell_type:
                        count += 1
        return count
        
    def randomize(self, cell_type_registry, fill_ratio=1.0):
        """
        Randomize the matrix cells based on cell type hotness values.
        
        :param cell_type_registry: The registry containing cell types and hotness values
        :param fill_ratio: The percentage of cells to randomize (0.0-1.0)
        """
        # Get all cells as a flat list
        all_cells = []
        for y in range(self.height):
            for x in range(self.width):
                all_cells.append((x, y))
                
        # Calculate number of cells to fill
        num_to_fill = int(len(all_cells) * fill_ratio)
        
        # Randomly select cells to fill
        cells_to_fill = random.sample(all_cells, num_to_fill)
        
        # Set random types based on hotness
        for x, y in cells_to_fill:
            cell_type = cell_type_registry.get_random_type()
            self.cells[y][x].type = cell_type
