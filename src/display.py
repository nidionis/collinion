import pygame
import sys

class Display:
    def __init__(self, field, kinds):
        self.field = field
        self.kinds = kinds
        self.cell_size = 480 // max(field.width, field.height)
        pygame.init()
        self.window = pygame.display.set_mode((480, 480))
        self.title = "Cell Matrix Simulator"
        pygame.display.set_caption(self.title)
        
        # Generate color map from registry
        self.colors = {}
        self.update_colors()
    
    def update_colors(self):
        """Update color mapping from registry"""
        for type_name in self.kinds.get_types():
            self.colors[type_name] = self.kinds.(type_name)
    
    def render(self):
        self.window.fill((0, 0, 0))
        for y in range(self.field.height):
            for x in range(self.field.width):
                color = self.colors.get(self.field.cells[y][x].type, (100, 100, 100))
                pygame.draw.rect(
                    self.window, 
                    color, 
                    (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                )
        pygame.display.flip()
    
    def run(self, rules):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False
            
            self.field = self.field.apply_rules(rules)
            self.render()
            clock.tick(1000)
        
        pygame.quit()
        sys.exit()
