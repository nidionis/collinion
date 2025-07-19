import pygame
import sys
import rules
import numpy as np
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
        try:
            self.set_cell_size()
        except ZeroDivisionError:
            exit("Window size too small")

        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.title = self.DEFAULT_TITLE
        pygame.display.set_caption(self.title)

        # Frame rate management
        self.frame_rate = 5
        self.target_frame_rate = 30
        self.max_achieved_fps = 0
        self.fps_history = [0] * 10  # Track recent FPS values
        self.history_index = 0
        self.frame_lock = False      # Indicates if we've hit machine limits

        # Color management
        self.colors = {}
        self.color_cache = {}
        
        # Performance optimization
        self.cell_surface = pygame.Surface((self.win_width, self.win_height))
        self.fps_font = pygame.font.Font(None, 36)
        self.show_fps = False
        self.last_fps = 0
        self.render_time = 0
        self.update_time = 0
        
        # Key press tracking for debouncing
        self.last_key_press = {
            'p': 0,
            'f': 0,
            'r': 0
        }

    def set_cells(self, cells):
        self.game.field.cells = cells

    def set_cell_size(self):
        w_ratio = self.win_width // self.height
        h_ratio = self.win_width // self.height
        if w_ratio > h_ratio:
            self.cell_size = self.win_width // self.width
        else:
            self.cell_size = self.win_height // self.height

    def display_fps_info(self):
        """Display FPS and performance information on screen"""
        if not self.show_fps:
            return
            
        # Choose color based on performance status
        status_color = (255, 255, 0) if self.frame_lock else (255, 255, 255)
        
        # Render FPS information
        fps_text = self.fps_font.render(
            f"FPS: {self.last_fps:.1f}/{self.target_frame_rate:.1f} Max: {self.max_achieved_fps:.1f}", 
            True, status_color
        )
        
        # Render performance metrics
        perf_text = self.fps_font.render(
            f"Render: {self.render_time*1000:.1f}ms Update: {self.update_time*1000:.1f}ms", 
            True, (255, 255, 255)
        )
        
        # Render status information
        status = "MAXED OUT" if self.frame_lock else "Normal"
        status_text = self.fps_font.render(status, True, status_color)
        
        # Draw all text elements
        self.window.blit(fps_text, (10, 10))
        self.window.blit(perf_text, (10, 50))
        self.window.blit(status_text, (10, 90))
    
    def render(self):
        start_time = time.time()
        
        # Clear both surfaces
        self.window.fill((0, 0, 0))
        self.cell_surface.fill((0, 0, 0))
        
        # Draw all cells on the buffer surface
        for cell in self.game:
            cell_str = str(cell)
            if cell_str not in self.color_cache:
                color_name = self.kinds.color(cell)
                try:
                    # Try to convert the color name to RGB using pygame
                    self.color_cache[cell_str] = pygame.Color(color_name)
                except ValueError:
                    # Fall back to our defined colors if pygame doesn't recognize it
                    if hasattr(self.kinds, 'colors') and color_name in self.kinds.colors:
                        rgb = self.kinds.colors[color_name]
                        self.color_cache[cell_str] = pygame.Color(rgb[0], rgb[1], rgb[2])
                    else:
                        # Default to white if color not found
                        self.color_cache[cell_str] = pygame.Color('white')
            
            color_rgb = self.color_cache[cell_str]
            pygame.draw.rect(
                self.cell_surface, 
                color_rgb, 
                (cell.x * self.cell_size, cell.y * self.cell_size,
                 self.cell_size, self.cell_size)
            )
        
        # Blit the entire cell surface at once
        self.window.blit(self.cell_surface, (0, 0))
        
        # Display FPS and performance information
        self.display_fps_info()
            
        pygame.display.flip()
        
        self.render_time = time.time() - start_time

    def handle_key_press(self, key, action, debounce_time=0.3):
        """Handle key press with debouncing"""
        current_time = time.time()
        if current_time - self.last_key_press.get(key, 0) > debounce_time:
            action()
            self.last_key_press[key] = current_time
            return True
        return False
    
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            keys = pygame.key.get_pressed()
            
            # Speed adjustments with machine limit detection
            if keys[pygame.K_UP]:
                # Store previous target for comparison
                prev_target = self.target_frame_rate
                
                # If not at machine limits, increase target
                if not self.frame_lock:
                    self.target_frame_rate = min(10000, self.target_frame_rate * 1.2)
                else:
                    # If at max, ensure we're still pushing limits
                    self.target_frame_rate = self.max_achieved_fps * 1.2
                
                # Apply the new target
                self.frame_rate = self.target_frame_rate
                
            if keys[pygame.K_DOWN] and self.target_frame_rate > 1:
                # Always allow slowing down
                self.target_frame_rate /= 1.2
                self.frame_rate = self.target_frame_rate
                # When slowing down, we're not at machine limits
                self.frame_lock = False
            
            # Toggle FPS display with P or F key
            if keys[pygame.K_p]:
                self.handle_key_press('p', lambda: setattr(self, 'show_fps', not self.show_fps))
                
            if keys[pygame.K_f]:
                self.handle_key_press('f', lambda: setattr(self, 'show_fps', not self.show_fps))
                
            # Reset to default speed with R
            if keys[pygame.K_r]:
                self.handle_key_press('r', lambda: self._reset_speed())
                
            if keys[pygame.K_q] or keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                running = False
                
            # Measure update time
            update_start = time.time()
            self.game.switch_all()
            self.update_time = time.time() - update_start
            
            self.render()
            
            # Calculate actual FPS and check if we've hit machine limits
            self.last_fps = clock.get_fps()
            
            # Update FPS history for stability
            self.fps_history[self.history_index] = self.last_fps
            self.history_index = (self.history_index + 1) % len(self.fps_history)
            avg_fps = sum(self.fps_history) / len(self.fps_history)
            
            # Update the max achieved FPS if we've reached a new high
            if avg_fps > self.max_achieved_fps:
                self.max_achieved_fps = avg_fps
            
            # Check if we've hit machine limits (actual FPS significantly below target)
            if self.target_frame_rate > 30 and avg_fps < self.target_frame_rate * 0.8:
                # We've hit the machine's limit
                self.frame_lock = True
                # Set target to slightly above max achieved for stability
                self.target_frame_rate = self.max_achieved_fps * 1.05
                self.frame_rate = self.target_frame_rate
            
            # Try to hit the target frame rate
            clock.tick(self.frame_rate)
            
        pygame.quit()
        sys.exit()
        
    def _reset_speed(self):
        """Reset speed to default"""
        self.target_frame_rate = 30
        self.frame_rate = 30
        self.frame_lock = False
