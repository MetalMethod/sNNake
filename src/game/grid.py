class Grid:
    def __init__(self, GRID_CELL_SIZE, color, pygame, screen, MAP_SIZE):
        self.cell_size = GRID_CELL_SIZE
        self.MAP_SIZE = MAP_SIZE
        self.rows = self.cell_size
        self.columns = self.cell_size
        self.center_x = (self.columns / 2)        
        self.center_y = (self.rows / 2)
        self.color = color
        self.pygame = pygame
        self.screen = screen

    def draw(self):
        for y in range(self.rows):
            point1 = (0, self.cell_size * y)
            point2 = (self.MAP_SIZE, self.cell_size * y)
            self.pygame.draw.lines(self.screen, self.color, False, [point1,point2], 1)
            
            for x in range(self.columns):
                point1 = (self.cell_size * x, 0)
                point2 = (self.cell_size * x, self.MAP_SIZE )
                self.pygame.draw.lines(self.screen, self.color, False, [point1,point2], 1)
                            
    def get_grid_rows(self):
        return self.rows
                
class Position:
    def __init__(self):
        self.set_position(0, 0)
        
    def get_position(self):
        return (self.x, self.y)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        