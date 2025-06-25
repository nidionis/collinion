#!/usr/bin/env python3

from classes.Cell import Cell, CellType
from classes.Grid import Grid
from classes.display import display_game

def main():
    CellType("ALIVE", "blue",3)
    CellType("DEAD", "red")
    grid = Grid(CellType, 30, 15)
    grid.create_random_grid()
    display = display_game(grid, width=800, height=600, title="Color Palette Viewer")
    display.display_grid()

if __name__ == "__main__":
    main()
