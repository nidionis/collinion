import pygame
import sys
import rules
import numpy as np
import time
import time


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
        
        # Create performance optimization surfaces
        self.cell_surface = pygame.Surface((self.win_width, self.win_height))
        
        # Performance monitoring
        self.fps_font = pygame.font.Font(None, 36)
        self.show_fps = True
        self.last_fps = 0
        self.render_time = 0
        self.update_time = 0
        
        # Create a cell buffer surface for faster rendering
        self.cell_surface = pygame.Surface((self.win_width, self.win_height))
        self.fps_font = pygame.font.Font(None, 36)
        self.show_fps = True
        self.last_fps = 0
        
        # Performance tracking
        self.render_time = 0
        self.update_time = 0

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
        start_time = time.time()
        
        # Clear both surfaces
        self.window.fill((0, 0, 0))
        self.cell_surface.fill((0, 0, 0))
        
        # Draw all cells on the buffer surface
        for cell in self.game:
            cell_str = str(cell)
            if cell_str not in self.color_cache:
                self.color_cache[cell_str] = self.kinds.color(cell)
            
            color_rgb = self.color_cache[cell_str]
            pygame.draw.rect(
                self.cell_surface, 
                color_rgb, 
                (cell.x * self.cell_size, cell.y * self.cell_size,
                 self.cell_size, self.cell_size)
            )
        
        # Blit the entire cell surface at once
        self.window.blit(self.cell_surface, (0, 0))
        
        # Display FPS if enabled
        if self.show_fps:
            fps_text = self.fps_font.render(f"FPS: {self.last_fps:.1f}", True, (255, 255, 255))
            perf_text = self.fps_font.render(f"Render: {self.render_time*1000:.1f}ms Update: {self.update_time*1000:.1f}ms", True, (255, 255, 255))
            self.window.blit(fps_text, (10, 10))
            self.window.blit(perf_text, (10, 50))
            
        pygame.display.flip()
        
        self.render_time = time.time() - start_time

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                pass
            if keys[pygame.K_RIGHT]:
                pass
            if keys[pygame.K_UP] and self.frame_rate < 1000:
                self.frame_rate *= 1.2
            if keys[pygame.K_DOWN] and self.frame_rate > 0.3:
                self.frame_rate /= 1.2
            if keys[pygame.K_f]:
                self.show_fps = not self.show_fps
            if keys[pygame.K_q] or keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                running = False
                
            # Measure update time
            update_start = time.time()
            self.game.switch_all()
            self.update_time = time.time() - update_start
            
            self.render()
            
            # Calculate actual FPS
            self.last_fps = clock.get_fps()
            clock.tick(self.frame_rate)
            
        pygame.quit()
        sys.exit()
