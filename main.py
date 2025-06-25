#!/usr/bin/env python3

from classes.Cell import Cell, CellType
from classes.Grid import Grid
from classes.display import display_game

def rules(cell: Cell, cell_types: CellType):
    if cell == "ALIVE":
        cell = "DEAD"

def apply_rules(grid: Grid, cell_types: CellType):
    for row in grid.cells:
        for cell in row:
            rules(cell, cell_types)

def main():
    CellType("ALIVE", "blue",3)
    CellType("DEAD", "red")
    grid = Grid(CellType, 30, 15)
    grid.create_random_grid()
    display = display_game(grid, width=800, height=600, title="Color Palette Viewer")
    display.display_grid()
    time.sleep(1)
    while True:
        apply_rules(grid, grid.cell_types)
        display.clear_screen()

if __name__ == "__main__":
    main()
