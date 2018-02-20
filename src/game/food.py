from random import randint

class Food:
    def __init__(self, size, grid_rows, grid_columns):
        self.size = size
        self.alive = True
        self.grid_rows = grid_rows
        self.grid_columns = grid_columns
        self.position = []
        self.spawn()

    def draw(self, pygame, screen, color):
        pygame.draw.rect(screen, color, ((self.size * self.position[0] +self.size/4), (self.size * self.position[1] +self.size/4), self.size/2, self.size/2))

    def spawn(self):
        x = randint(1, self.grid_columns - 1)
        y = randint(1, self.grid_rows - 1)
        self.position = [x, y]
        #self.debug()
        
    def detect_colision(self, player):
        if(player.position[0] == self.position[0] and player.position[1] == self.position[1]):
            self.spawn()
            player.eat()
            return True

    def debug(self):
        print("food spawned at x: " + str(self.position[0]) + " y: " + str(self.position[1]) )
        return