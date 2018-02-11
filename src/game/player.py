from random import randint
from grid import Position

class Player:
    def __init__(self, x, y, size):
        self.position = Position()        
        self.position.x = x 
        self.position.y = y
        self.size = size
        self.alive = True
        self.direction = self.initial_direction()

    def draw(self, pygame, screen, color):
        pygame.draw.rect(screen, color, (self.position.x * self.size, self.position.y * self.size, self.size, self.size))

    def up(self):
        self.position.y = self.position.y - 1
        
    def right(self):
        self.position.x = self.position.x + 1
                
    def down(self):
        self.position.y = self.position.y + 1
     
    def left(self):
        self.position.x = self.position.x - 1
     
    def initial_direction(self):
        return randint(1, 4)

    def detect_walls(self, grid):
        if(self.position.x > grid.columns - 1):
            self.position.x = grid.columns - 1
            self.alive = False

        if(self.position.x < 0):
            self.position.x = 0
            self.alive = False

        if(self.position.y > grid.rows - 1):
            self.position.y = grid.rows - 1
            self.alive = False

        if(self.position.y < 0):
            self.position.y = 0
            self.alive = False
        return    
    
    def move(self):
        if(self.direction == 1):
            self.up()
        if(self.direction == 2):
            self.right()
        if(self.direction == 3):
            self.down()
        if(self.direction == 4):
            self.left()
        return
            
