#!/usr/bin/env python3
from copy import deepcopy

from classes.Cell import Cell, CellType
from classes.Grid import Grid
from time import sleep

#implement as easely using __functions__ undurscored
def rules(cell: Cell, cell_types: CellType):
    if cell.around("ALIVE") < 2 or cell.around("ALIVE") > 3:
        return "DEAD"
    if cell.around("ALIVE") == 3:
        return "ALIVE"
    return cell

def apply_rules(grid: Grid, cell_types: CellType):
    new_grid = deepcopy(grid)
    for row in grid.cells:
        for cell in row:
            new_cell =  CellType.get(str(rules(cell, cell_types)))
            new_grid.set_cell(cell.x(), cell.y(), new_cell)
    new_grid.display_.grid = new_grid
    return new_grid

def main():
    CellType("ALIVE", "gReen",2)
    CellType("DEAD", "black")
    grid = Grid(CellType, 80, 80)
    grid.create_random_grid()
    while True:
        grid.display_frame()
        sleep(0.1)
        grid = apply_rules(grid, grid.cell_types)
        grid.display_.clear_screen()

if __name__ == "__main__":
    main()
