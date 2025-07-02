from cell_matrix.matrix import Matrix
from cell_matrix.display import Display
from cell_matrix.helpers import around
import random

def rules(cell, matrix):
    alive_neighbors = around(cell, matrix, "alive")
    
    if cell.type == "empty" and alive_neighbors == 3:
        return "alive"
    elif cell.type == "alive" and (alive_neighbors < 2 or alive_neighbors > 3):
        return "empty"
    return None

def main():
    matrix = Matrix(30, 21)
    
    # Random initial state
    for y in range(matrix.height):
        for x in range(matrix.width):
            if random.random() < 0.3:
                matrix.cells[y][x].type = "alive"
    
    display = Display(matrix)
    display.run(rules)

if __name__ == "__main__":
    main()
