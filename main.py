from cell_matrix.matrix import Matrix
from cell_matrix.display import Display
from cell_matrix.helpers import around
from cell_matrix.cell_types import CellTypeRegistry

def rules(cell, matrix):
    alive_neighbors = around(cell, matrix, "alive")
    
    if cell.type == "empty" and alive_neighbors == 3:
        return "alive"
    elif cell.type == "alive" and (alive_neighbors < 2 or alive_neighbors > 3):
        return "empty"
    return None

def main():
    # Initialize cell type registry with hotness values
    cell_types = CellTypeRegistry()
    cell_types.add_type("empty", "black", hotness=0)  # 0 hotness means won't appear randomly
    cell_types.add_type("alive", "white", hotness=30)
    
    # Create matrix
    matrix = Matrix(30, 21)
    
    # Randomize using registry - hotness values determine probabilities
    matrix.randomize(cell_types, fill_ratio=0.3)
    
    # Set up display with the right colors
    display = Display(matrix, cell_types)
    
    # Run simulation
    display.run(rules)

if __name__ == "__main__":
    main()
