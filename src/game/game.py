###### sNNake by metalMethod (github.com/metalMethod)

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
TIME_DELAY = 60
BODY_LENGTH = 3

# set up the colors
BLACK = (  30,  30,  30)
WHITE = (180, 180, 180)
GREY  = ( 10,  10,  10)
RED   = (180,   0,   0)
GREEN = (  0, 100,   0)
BLUE  = (  0,   0, 100)

class Game:
    def __init__(self, max_games):
        #setup
        pygame.init()
        pygame.display.set_caption('sNNake')
        self.icon = pygame.Surface((32,32))
        pygame.display.set_icon(self.icon)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.game_count = 1
        self.max_games = max_games
        self.main_loop()
       
    def init_game_objects(self):   
        self.grid = Grid(GRID_CELL_SIZE, GREY, pygame, self.screen, MAP_SIZE)
        self.player = Player(self.grid.center_x, self.grid.center_y, GRID_CELL_SIZE, BODY_LENGTH)
        self.food = Food(GRID_CELL_SIZE, self.grid.rows - 1, self.grid.columns - 1)
        self.controller = Controller(self.player)

    def observation(self):     
        return self.player, self.food

    def game_status(self):
        print("##### GAME START ##### game count: ", self.game_count)
    
    def main_loop(self):
        while (self.game_count <= self.max_games):
            self.game_status()
            self.init_game_objects()
            self.score = 0
            self.game_loop()
            self.game_count = self.game_count + 1

    def game_loop(self):
        #game loop
        while self.player.alive:
            #msElapsed = clock.tick(30)
            pygame.time.delay(TIME_DELAY)

            #game loop exit conditions
            if(pygame.key.get_pressed()[pygame.K_RETURN] == 1): break
            if(pygame.key.get_pressed()[pygame.K_ESCAPE] == 1): sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            # erase the screen
            self.screen.fill(BLACK)

            #draw objects
            self.food.draw(pygame, self.screen, WHITE)
            #draw body
            for el in self.player.body_list:
                el.draw(pygame, self.screen, WHITE)
            
            self.grid.draw()

            #update objects
            self.player.detect_walls(self.grid)
            self.player.detect_body()
            self.controller.update_player()
            if(self.food.detect_colision(self.player)):
                self.score = self.score + 1
                print("score: ", self.score)
            
            #update all and close the loop
            pygame.display.update()
        #close game loop

# if __name__ == "__main__":
#     g = Game(3)