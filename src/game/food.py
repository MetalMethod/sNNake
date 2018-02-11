from random import randint

class Food:
    def __init__(self, size, MAP_SIZE):
        self.size = size
        self.alive = True
        self.MAP_SIZE = MAP_SIZE
        self.initial_position()
        self.grid_size = self.MAP_SIZE / self.size

    def draw(self, pygame, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))
        self.screen = screen

    def initial_position(self):
        self.x = self.size * randint(0,self.size)
        self.y = self.size * randint(0,self.size)