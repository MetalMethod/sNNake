from random import randint
from grid import Position
class Food:
    def __init__(self, size, grid_rows, grid_columns):
        self.size = size
        self.alive = True
        self.grid_rows = grid_rows
        self.grid_columns = grid_columns
        self.position = Position()
        self.spawn()

    def draw(self, pygame, screen, color):
        pygame.draw.rect(screen, color, ((self.size * self.position.x +self.size/4), (self.size * self.position.y +self.size/4), self.size/2, self.size/2))

    def spawn(self):
        x = randint(1, self.grid_columns - 1)
        y = randint(1, self.grid_rows - 1)
        self.position.set_position(x, y)
        print("food spawned at x: " + str(self.position.x) + " y: " + str(self.position.y))
        
    def detect_colision(self, player):
        if(player.position.x == self.position.x and player.position.y == self.position.y):
            self.spawn()
            player.eat()