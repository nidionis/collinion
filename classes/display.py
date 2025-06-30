from __future__ import annotations
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.Grid import Grid


class display_game:

    def __init__(self, grid: Grid, width=800, height=600, title="Colinion"):
        """
        Initialize the PyGame display

        :param width: Window width
        :param height: Window height
        :param title: Window title
        """
        # Initialize pygame
        pygame.init()

        # Set up display
        self.grid = grid
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.cell_size = self.calc_cell_size()

        # Font setup
        self.font = pygame.font.SysFont('Arial', 16)
        self.title_font = pygame.font.SysFont('Arial', 24, bold=True)

        # Default colors and settings
        self.bg_color = (240, 240, 240)  # Light gray background
        self.text_color = (10, 10, 10)  # Almost black text
        self.colors = {}  # Will be populated with color data

        # For animations/transitions
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.setup_colors()

    def calc_cell_size(self):
        height = self.height / self.grid.height
        width = self.width / self.grid.width
        return min(width, height)

    def setup_colors(self):
        """
        Populates self.colors with colors from CellType for every type in grid._types.
        Each entry is cell_type: color.
        """
        for name, cell_type in self.grid.cell_types._types.items():
            self.colors[name] = cell_type.color

    def clear_screen(self):
        """
        Clear the display by filling it with the background color
        """
        self.screen.fill(self.bg_color)

    def display_cell(self, position: (int, int)):
        cell = self.grid.get_cell(*position)
        x, y = position
        box = pygame.Rect(x * self.cell_size,
                          y * self.cell_size,
                          self.cell_size,
                          self.cell_size)
        pygame.draw.rect(self.screen, self.colors[cell.type.name], box)

    def display_row(self, row):
        for cell in row:
            self.display_cell(cell.position)

    def display_grid(self):
        for row in self.grid.cells:
            self.display_row(row)
        pygame.display.flip()  # This line was commented out, which means nothing will show

        ## Add event handling to keep the window open
        #running = True
        #while running:
        #    for event in pygame.event.get():
        #        if event.type == pygame.QUIT:
        #            pygame.quit()
        #            sys.exit()
        #    self.clock.tick(self.fps)