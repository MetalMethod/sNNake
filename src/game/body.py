from grid import Position

class Body:
        def __init__(self, x, y, size):
            self.position = Position()
            self.position.x = x 
            self.position.y = y
            self.previous_position = Position()
            self.size = size
            
        def draw(self, pygame, screen, color):
            pygame.draw.rect(screen, color, (self.position.x * self.size, self.position.y * self.size, self.size, self.size))

        def info(self):
            print(self.position.get_position())