import pygame
import sys
import rules


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

        self.frame_rate = 60
        self.colors = {}

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
        for cell in self.game:
            color_rgb = self.kinds.color(cell)

            pygame.draw.rect(
                self.window,
                color_rgb,
                (cell.x * self.cell_size, cell.y * self.cell_size,
                 self.cell_size, self.cell_size)
            )
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    continue
                if keys[pygame.K_RIGHT]:
                    continue
                if keys[pygame.K_UP] and self.frame_rate < 1000:
                    self.frame_rate *= 1.2
                    continue
                if keys[pygame.K_DOWN] and self.frame_rate > 0.5:
                    self.frame_rate /= 1.2
                    continue
                if  keys[pygame.K_q] or keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                    running = False
            self.game.switch_all()
            self.render()
            clock.tick(self.frame_rate)
        pygame.quit()
        sys.exit()
