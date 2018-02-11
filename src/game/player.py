from random import randint

class Player:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.alive = True
        self.direction = self.initial_direction()

    def draw(self, pygame, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))

    def up(self):
        self.y = self.y - self.speed
        return

    def right(self):
        self.x = self.x + self.speed
        return
        
    def down(self):
        self.y = self.y + self.speed
        return

    def left(self):
        self.x = self.x - self.speed
        return

    def initial_direction(self):
        return randint(1, 4)

    def detect_walls(self, MAP_SIZE):
        if(self.x > MAP_SIZE - self.size):
            self.x = MAP_SIZE - self.size
            self.alive = False

        if(self.x < 0):
            self.x = 0
            self.alive = False

        if(self.y > MAP_SIZE - self.size):
            self.y = MAP_SIZE - self.size
            self.alive = False

        if(self.y < 0):
            self.y = 0
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
            
