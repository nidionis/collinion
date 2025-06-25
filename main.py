#!/usr/bin/env python3

"""
This version uses simple text characters to display the game grid.
"""

import os
import time
import random
from classes.Cell import Cell, CellType
from classes.Grid import Grid
from classes.display import display_game


#def main():
#    """Main function for testing purpose"""
#    CellType("ALIVE", "#00FF00")
#    CellType("DEAD", "#FF00FF")
#    # But can be a lot others
#
#    # Create a grid with random cells using defined cell types
#    grid = Grid(CellType, 30, 15)
#    grid.create_random_grid()
#    grid.display()
#    #try:
#    #    # Main game loop
#    #    while True:
#    #        display_grid(grid)
#    #        update_grid(grid)
#    #        time.sleep(UPDATE_INTERVAL)
#    #except KeyboardInterrupt:
#    #    print("\nExiting Game of Life. Goodbye!")


def main():
    # Your existing color dictionary
    BASIC_COLORS = {
        # Primary Colors
        'RED': {'hex': '#FF0000'},
        'GREEN': {'hex': '#00FF00'},
        'BLUE': {'hex': '#0000FF'},

        # Secondary Colors
        'YELLOW': {'hex': '#FFFF00'},
        'PURPLE': {'hex': '#800080'},
        'ORANGE': {'hex': '#FFA500'},

        # Neutral and Additional Colors
        'BLACK': {'hex': '#000000'},
        'WHITE': {'hex': '#FFFFFF'},
        'GRAY': {'hex': '#808080'},
        'CYAN': {'hex': '#00FFFF'}
    }

    import argparse
    parser = argparse.ArgumentParser(description='PyGame Color Display')
    parser.add_argument('-m', '--mode',
                        choices=['grid', 'wheel', 'interactive'],
                        default='interactive',
                        help='Display mode')
    args = parser.parse_args()

    # Create the display
    CellType("ALIVE", "#00FF00")
    CellType("DEAD", "#FF00FF")
    grid = Grid(CellType, 30, 15)
    grid.create_random_grid()
    display = display_game(grid, width=800, height=600, title="Color Palette Viewer")
    display.display_grid()


if __name__ == "__main__":
    main()
