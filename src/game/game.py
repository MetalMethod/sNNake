###### first sketch of sNNake
#dependencies
import sys
import pygame


#other classes from same folder
from controller import Controller
from grid import Grid
from player import Player
from food import Food

#constants
MAP_SIZE = 400 
WINDOW_SIZE = width, height = MAP_SIZE, MAP_SIZE
GRID_CELL_SIZE = 20
TIME_DELAY = 60
BODY_LENGTH = 3

# set up the colors
BLACK = (  30,  30,  30)
WHITE = (180, 180, 180)
GREY  = ( 10,  10,  10)
RED   = (180,   0,   0)
GREEN = (  0, 100,   0)
BLUE  = (  0,   0, 100)

#setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

#instantiate the player controller object
controller = Controller()
  
#instantiate the game objects
grid = Grid(GRID_CELL_SIZE, GREY, pygame, screen, MAP_SIZE)
player = Player(grid.center_x, grid.center_y, GRID_CELL_SIZE, BODY_LENGTH)
food = Food(GRID_CELL_SIZE, grid.rows - 1, grid.columns - 1)

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
    food.draw(pygame, screen, WHITE)
    #draw body
    for el in player.body_list:
        el.draw(pygame, screen, WHITE)
    
    grid.draw()

    #update objects
    controller.update_player(player, grid)
    food.detect_colision(player)
    
    #update all and close the loop
    pygame.display.update()
#close game loop
