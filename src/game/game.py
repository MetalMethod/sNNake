###### sNNake by metalMethod (github.com/metalMethod)
#
#

#dependencies
import sys
import pygame

#other classes from same folder
from game.controller import Controller
from game.grid import Grid
from game.player import Player
from game.food import Food

#constants
MAP_SIZE = 400 
WINDOW_SIZE = width, height = MAP_SIZE, MAP_SIZE
GRID_CELL_SIZE = 20
TIME_DELAY = 100
BODY_LENGTH = 4

# set up the colors
BLACK = (  30,  30,  30)
WHITE = (180, 180, 180)
GREY  = ( 10,  10,  10)
RED   = (180,   0,   0)
GREEN = (  0, 100,   0)
BLUE  = (  0,   0, 100)

class Game:
    def __init__(self, max_games):
        pygame.init()
        pygame.display.set_caption('sNNake')
        self.icon = pygame.Surface((32,32))
        pygame.display.set_icon(self.icon)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.count = 1
        self.max_games = max_games
        self.init_game_objects()
    
    def init_game_objects(self):   
        self.grid = Grid(GRID_CELL_SIZE, GREY, pygame, self.screen, MAP_SIZE)
        self.player = Player(self.grid.center_x, self.grid.center_y, GRID_CELL_SIZE, BODY_LENGTH)
        self.food = Food(GRID_CELL_SIZE, self.grid.rows - 1, self.grid.columns - 1)
        self.controller = Controller(self.player)

    def game_status(self):
        #print("##### GAME START ##### game count: ", self.count)
        return
    
    def draw(self):
        # erase the screen
        self.screen.fill(BLACK)
        #draw objects
        self.food.draw(pygame, self.screen, WHITE)
        #draw body
        for el in self.player.body_list:
            el.draw(pygame, self.screen, WHITE)
        
        self.grid.draw()

    def exit_conditions(self):
        if(pygame.key.get_pressed()[pygame.K_RETURN] == 1): return #break
        if(pygame.key.get_pressed()[pygame.K_ESCAPE] == 1): sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
             
    def check_isAlive(self, sensors):
        if(sensors.detect_walls(self.grid, self.player.position)): 
            self.player.alive = False
            #self.player.position = [10,10]
            #print("WALL HIT")
        
        if(sensors.detect_body(self.player.position)): 
            self.player.alive = False
            #print("BODY HIT")
        return

    def reset(self):
        self.init_game_objects()
        self.score = 0

    def update_objects(self, sensors):
        self.controller.detect_keyboard()            
        self.player.turn()
        self.player.update_body()
        self.check_isAlive(sensors)      
        if(self.food.detect_colision(self.player)):
            self.score = self.score + 1

    ### update pygame and close the step        
    def finish_step(self):
        #msElapsed = clock.tick(30)
        pygame.display.update()            
        pygame.time.delay(TIME_DELAY)

    def observation(self):     
        return self.player, self.food
    
    # concept of step function from open ai: one step receaves a input and generates a observation.
    def step(self, sensors, action):
        self.exit_conditions()
        self.draw()
        self.update_objects(sensors)
        self.controller.input(action)
        
        ### STEP OBSERVATION CODE


        ### update all and close the step
        self.finish_step()
    #end of step
