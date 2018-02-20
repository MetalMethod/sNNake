import pygame
import numpy as np

class Controller:

    def __init__(self, player):
        self.player = player

    # API input
    def step(self, direction):
        if(direction == 1):
            self.up()
        if(direction == 2):
            self.right()
        if(direction == 3):
            self.down()
        if(direction == 4):
            self.left()
    
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
            player.eat()
    
    def update_player(self):
        self.detect_keyboard()
        self.player.turn()
        self.player.update_body()
        #self.debug()
    
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
