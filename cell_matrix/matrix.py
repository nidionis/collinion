from cell_matrix.cell import Cell

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
