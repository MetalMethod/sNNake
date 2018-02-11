class Grid:

    def __init__(self, GRID_CELL_SIZE, color, pygame, screen):
        self.cell_size = GRID_CELL_SIZE
        self.rows = self.cell_size
        self.columns = self.cell_size
        self.color = color
        self.pygame = pygame
        self.screen = screen

    def draw(self):
        for y in range(self.rows):
            for x in range(self.columns):
                rect = self.pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                self.pygame.draw.rect(self.screen, self.color, rect, 1)

                #self.pygame.draw.rect(self.cell_size * self.cell_size, self.color, rect)