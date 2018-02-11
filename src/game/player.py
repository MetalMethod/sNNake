from random import randint
from grid import Position
from body import Body

class Player:
    def __init__(self, x, y, size):
        self.position = Position()        
        self.position.x = x 
        self.position.y = y
        self.previous_position = Position()
        self.size = size
        self.alive = True
        self.direction = self.initial_direction()
        self.body_list = []
        self.eat()
        self.eat()
        

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
    
    def turn(self):
        if(self.direction == 1):
            self.up()
        if(self.direction == 2):
            self.right()
        if(self.direction == 3):
            self.down()
        if(self.direction == 4):
            self.left()
        return
            
    def eat(self):
        segment = Body(self.previous_position.x, self.previous_position.y, 20)
        self.body_list.append(segment)
       # print(len(self.body_list)-1)
        print("eat")

    def update_body(self):
        for segment in self.body_list:
            segment.position.x = self.previous_position.x
            segment.position.y = self.previous_position.y
            segment.previous_position.x = segment.position.x
            segment.previous_position.y = segment.position.y

        self.previous_position.x = self.position.x
        self.previous_position.y = self.position.y
        
    # def last_body_position(self):
    # #     if (len(self.body_list) ):
    #     self.body_list[len(self.body_list)].position = self.body_list[len(self.body_list)-1].previous_position
    #     return