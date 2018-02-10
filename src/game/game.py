###### first sketch of sNNake
#dependencies
import sys
import pygame

#other classes from same folder
from controller import Controller
from player import Player

#constants
WINDOW_SIZE = width, height = 400, 400
CENTER =  WINDOW_SIZE[0] / 2
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
  
#instantiate the player(initial_x, initial_y, speed)
head = Player(CENTER, CENTER, 10, 1)

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
    head.draw(pygame, screen, WHITE, GRID_CELL_SIZE)
    
    #update objects
    controller.update_player(head)

    #update all and close the loop
    pygame.display.update()
#close game loop
