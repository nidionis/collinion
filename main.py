#!/usr/bin/env python3

"""
Conway's Game of Life - Basic Console Version
This version uses simple text characters to display the game grid.
"""

import os
import time
import random
from classes.Cell import Cell, CellType
from classes.Grid import Grid

def main():
    """Main function for testing purpose"""
    CellType("ALIVE", "#00FF00")
    CellType("DEAD", "#FF00FF")
    # But can be a lot others

    # Create a grid with random cells using defined cell types
    grid = Grid(CellType, 30, 15)
    grid.create_random_grid()
    #try:
    #    # Main game loop
    #    while True:
    #        display_grid(grid)
    #        update_grid(grid)
    #        time.sleep(UPDATE_INTERVAL)
    #except KeyboardInterrupt:
    #    print("\nExiting Game of Life. Goodbye!")

if __name__ == "__main__":
    main()
