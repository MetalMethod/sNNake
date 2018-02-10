class Cat:
    def __init__(self, x, y, speed, initial_direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.initial_direction = initial_direction
    
    def draw(self, pygame, screen, color, size):
        pygame.draw.rect(screen, color, (self.x, self.y, size, size))

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

    def checkLimits(self):
        if(self.x > 400):
            self.x = 0

        if(self.x < 0):
            self.x = 400

        if(self.y > 400):
            self.y = 0

        if(self.y < 0):
            self.y = 400 

        return    