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
        pygame.draw.rect(screen, color, ((self.size * self.position.x +self.size/4), (self.size * self.position.y +self.size/4), self.size/2, self.size/2))

    def initial_position(self):
        x = randint(0,self.size)
        y = randint(0,self.size)
        self.position = Position()
        self.position.set_position(x, y)
        print("food created at x: " + str(self.position.x) + " y: " + str(self.position.y))
        
