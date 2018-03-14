from random import randint

import numpy as np

class Player:
    def __init__(self, x, y, size, BODY_LENGTH):
        self.position = [x, y]
        self.size = size
        self.alive = True
        self.food = False
        self.direction = self.initial_direction()
        self.body_list = []
        #self.insert_body(BODY_LENGTH)
        self.insert_body(1)
    
    def initial_direction(self):
        return randint(1, 4)
    
    def draw(self, pygame, screen, color):
        pygame.draw.rect(screen, color, (self.position[0] * self.size, self.position[1] * self.size, self.size, self.size))

    def up(self):
        self.position[1] = self.position[1] - 1
        
    def right(self):
        self.position[0] = self.position[0] + 1
                
    def down(self):
        self.position[1] = self.position[1] + 1
    
    def left(self):
        self.position[0] = self.position[0] - 1
    
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
    
    def insert_body(self, number_of_segments):
        for i in range(number_of_segments):
            segment = Body(self.position[0], self.position[1], 20)
            self.body_list.insert(0, segment)
    
    def eat(self):
        self.food = True    
        
    def update_body(self):
        self.insert_body(1)

        if(self.food == False):
            self.body_list.pop()
        else:
            self.food = False

class Body:
        def __init__(self, x, y, size):
            self.position = [x, y]
            self.size = size
            
        def draw(self, pygame, screen, color):
            pygame.draw.rect(screen, color, (self.position[0] * self.size, self.position[1] * self.size, self.size, self.size))
