###### first sketch of sNNake
#dependencies
import sys
import pygame

#other classes from same folder
from controller import Controller
from player import Player

#constants
MAP_SIZE = 400 
WINDOW_SIZE = width, height = MAP_SIZE, MAP_SIZE
CENTER =  MAP_SIZE / 2
GRID_CELL_SIZE = 20
TIME_DELAY = 20

# set up the colors
BLACK = (  30,  30,  30)
WHITE = (180, 180, 180)
RED   = (100,   0,   0)
GREEN = (  0, 100,   0)
BLUE  = (  0,   0, 100)

#setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

#instantiate the player controller object
controller = Controller()
  
#instantiate the player(initial_x, initial_y, speed, direction)
head = Player(CENTER, CENTER, GRID_CELL_SIZE, 10)

#game loop
while 1:
    #msElapsed = clock.tick(30)
    pygame.time.delay(TIME_DELAY)

    #game loop exit conditions
    if(pygame.key.get_pressed()[pygame.K_ESCAPE] == 1): sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    # erase the screen
    screen.fill(BLACK)

    #draw objects
    head.draw(pygame, screen, WHITE)
    
    #update objects
    controller.update_player(head, MAP_SIZE)

    #update all and close the loop
    pygame.display.update()
#close game loop
