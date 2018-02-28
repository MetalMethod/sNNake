import pygame
import numpy as np

class Controller:

    def __init__(self, player):
        self.player = player

    ##### API input
    # action is -1 turn left, 
    # 0 do nothing and go forward 
    # 1 is turn rightt
    def input(self, action):
        if(action == -1):
            #turn left
            if(self.player.direction == 1):
                self.left()
            if(self.player.direction == 2):
                self.up()
            if(self.player.direction == 3):
                self.right()
            if(self.player.direction == 4):
                self.down()
            return
        if(action == 1):
            #turn right
            if(self.player.direction == 1):
                self.right()
            if(self.player.direction == 2):
                self.down()
            if(self.player.direction == 3):
                self.left()
            if(self.player.direction == 4):
                self.up()
            return
        if(action == 0):
            return
    
    def detect_keyboard(self):
        if (pygame.key.get_pressed()[pygame.K_UP] == 1):
            self.up()
        if (pygame.key.get_pressed()[pygame.K_RIGHT] == 1):
            self.right()
        if (pygame.key.get_pressed()[pygame.K_DOWN] == 1):
            self.down()
        if (pygame.key.get_pressed()[pygame.K_LEFT] == 1):
            self.left()
        if (pygame.key.get_pressed()[pygame.K_1] == 1):
            self.player.eat()
    
    def up(self):
        if (self.player.direction != 3) : self.player.direction = 1

    def right(self):
        if (self.player.direction != 4) : self.player.direction = 2

    def down(self):
        if (self.player.direction != 1) : self.player.direction = 3

    def left(self):
        if (self.player.direction != 2) : self.player.direction = 4

    def debug(self):
        #print(self.player.position_vector)
        # print("##########################")
        # for el in self.player.body_list:
        #     print (el.position.get_position())
        return
