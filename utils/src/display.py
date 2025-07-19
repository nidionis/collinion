import pygame
import sys
import rules
import numpy as np


class Display:
    DEFAULT_TITLE = "Collinion"

    def __init__(self, game, win_width=None, win_height=None):
        self.win_width = win_width
        if win_width == None:
            self.win_width = pygame.display.Info().current_w
        self.win_height = win_height
        if win_height == None:
            self.win_height = pygame.display.Info().current_h
        self.game = game
        self.height = self.game.height
        self.width = self.game.width
        self.kinds = self.game.kinds
        self.set_cell_size()

        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.title = self.DEFAULT_TITLE
        pygame.display.set_caption(self.title)

        self.frame_rate = 30
        self.colors = {}
        # Color cache for faster rendering
        self.color_cache = {}

    def set_cells(self, cells):
        self.game.field.cells = cells

    def set_cell_size(self):
        w_ratio = self.win_width // self.height
        h_ratio = self.win_width // self.height
        if w_ratio > h_ratio:
            self.cell_size = self.win_width // self.width
        else:
            self.cell_size = self.win_height // self.height

    def render(self):
        self.window.fill((0, 0, 0))
        
        # Pre-create all rectangles in one batch
        rects = []
        colors = []
        
        for cell in self.game:
            cell_str = str(cell)
            if cell_str not in self.color_cache:
                self.color_cache[cell_str] = self.kinds.color(cell)
            
            color_rgb = self.color_cache[cell_str]
            rect = pygame.Rect(
                cell.x * self.cell_size, 
                cell.y * self.cell_size,
                self.cell_size, 
                self.cell_size
            )
            rects.append(rect)
            colors.append(color_rgb)
        
        # Draw all rectangles at once if possible
        if len(rects) > 0:
            # Use either draw.rect for each or draw multiple if available
            for i, rect in enumerate(rects):
                pygame.draw.rect(self.window, colors[i], rect)
                
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            keys = pygame.key.get_pressed()
            # Fallback to the original method if cache isn't available
            if keys[pygame.K_LEFT]:
                pass
            if keys[pygame.K_RIGHT]:
                pass
            if keys[pygame.K_UP] and self.frame_rate < 1000:
                self.frame_rate *= 1.2
            if keys[pygame.K_DOWN] and self.frame_rate > 0.3:
                self.frame_rate /= 1.2
            if keys[pygame.K_q] or keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                running = False
                
            self.game.switch_all()
            self.render()
            clock.tick(self.frame_rate)
        pygame.quit()
        sys.exit()
