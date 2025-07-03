import pygame
import sys

class Display:
    def __init__(self, field, kinds):
        self.field = field
        self.kinds = kinds.kinds
        self.cell_size = 480 // max(field.width, field.height)
        pygame.init()
        self.window = pygame.display.set_mode((480, 480))
        self.title = "Cell Matrix Simulator"
        pygame.display.set_caption(self.title)
        
        # Generate color map from registry
        self.colors = {}
        self.update_colors()

    def update_colors(self):
        for key, val in self.kinds.items():
            self.colors[key] = val["color"]

    def render(self):
        self.window.fill((0, 0, 0))
        for y in range(self.field.height):
            for x in range(self.field.width):
                cell = self.field.cells[y][x]
                cell_kind_str = str(cell.kind)
                
                # Get the color name from the cell kind
                color_name = self.colors.get(cell_kind_str)
                
                # If we have a direct color mapping, use it
                if color_name in self.field.kinds.colors:
                    color_rgb = self.field.kinds.colors[color_name]
                else:
                    # Otherwise use a default color
                    color_rgb = (100, 100, 100)  # Default gray
                    
                pygame.draw.rect(
                    self.window, 
                    color_rgb, 
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
