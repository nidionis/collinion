#!/usr/bin/env python3

from classes.Cell import Cell, CellType
from classes.Grid import Grid
from time import sleep

#implement as easely using __functions__ undurscored
def rules(cell: Cell, cell_types: CellType):
    if cell == "ALIVE":
        return "DEAD"
    if cell == "DEAD":
        return "ALIVE"

def apply_rules(grid: Grid, cell_types: CellType):
    for row in grid.cells:
        for cell in row:
            new_cell =  CellType.get(rules(cell, cell_types))
            grid.set_cell(cell.x(), cell.y(), new_cell)
    return grid

def main():
    CellType("ALIVE", "blue",3)
    CellType("DEAD", "red")
    grid = Grid(CellType, 30, 15)
    grid.create_random_grid()
    while True:
        grid.display_frame()
        sleep(1)
        grid = apply_rules(grid, grid.cell_types)
        grid.display_.clear_screen()

if __name__ == "__main__":
    main()
