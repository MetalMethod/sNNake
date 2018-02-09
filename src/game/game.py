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
speed = [2, 2]
grid_cell_size = 20

# set up the colors
BLACK = (  30,  30,  30)
WHITE = (180, 180, 180)
RED   = (100,   0,   0)
GREEN = (  0, 100,   0)
BLUE  = (  0,   0, 100)

#setup
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(WINDOW_SIZE)

#instantiate the player controller object
controller = Controller()
  
#instantiate the player
head = Player(CENTER, CENTER, 10)

def draw_player(head):
    pygame.draw.rect(screen, WHITE, (head.x,head.y, grid_cell_size, grid_cell_size))
    return

#game loop
while 1:
    #msElapsed = clock.tick(30)
    pygame.time.delay(20)

    #game loop exit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # erase the screen
    screen.fill(BLACK)

    #draw objects
    draw_player(head)
    
    #update objects
    controller.update_player(head)

    #update all and close the loop
    pygame.display.update()
#close game loop
