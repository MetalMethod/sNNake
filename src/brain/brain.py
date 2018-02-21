# ANN DEPENDENCIES
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import tensorflow as af
# from sklearn.model_selection import train_test_split

import sys
sys.path.append('../') 
from game.game import Game

#constants
GAMES_COUNT = 3



# TO DO:
# add methods to detect if there is obstacles in left, forward or right, that return booleans
#
#


input = 0


class Brain:
    def __init__(self):
        self.game = Game(GAMES_COUNT)
        self.main_loop()


    # main_loop is a pool of games for training
    def main_loop(self):
        while (self.game.count <= self.game.max_games):
            #reseting game
            self.game.reset()
            
            # game loop
            while self.game.player.alive:
                
                self.game.observation()
                
                self.game.step(input)

            #end of game loop

            self.game.count = self.game.count + 1
            #print(self.game.observation())






if __name__ == "__main__":
    b = Brain()

