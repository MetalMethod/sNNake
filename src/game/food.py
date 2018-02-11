from random import randint
from grid import Position
class Food:
    def __init__(self, size, MAP_SIZE):
        self.size = size
        self.alive = True
        self.MAP_SIZE = MAP_SIZE
        self.grid_size = self.MAP_SIZE / self.size
        self.initial_position()

    def draw(self, pygame, screen, color):
        pygame.draw.rect(screen, color, (self.position.x, self.position.y, self.size, self.size))
        self.screen = screen

    def initial_position(self):
        x = self.size * randint(0,self.size)
        y = self.size * randint(0,self.size)
        self.position = Position()
        self.position.set_position(x, y)
        
