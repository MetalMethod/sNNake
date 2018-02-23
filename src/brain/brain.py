# ANN DEPENDENCIES
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import tensorflow as af
# from sklearn.model_selection import train_test_split

import sys
sys.path.append('../') 
from game.game import Game
from sensors import Sensors

#constants
GAMES_COUNT = 3

#globals
input = 0
observation = []

class Brain:
    def __init__(self):
        self.game = Game(GAMES_COUNT)
        
        self.main_loop()

    # main_loop is a pool of games for training
    def main_loop(self):
        while (self.game.count <= self.game.max_games):
            #reseting game
            self.game.reset()
            self.sensors = Sensors(self.game.grid, self.game.player)    
            # game loop
            while self.game.player.alive:
                
                # receive  observation
                observation = [self.sensors.obstacle_forward(), self.sensors.obstacle_left(), self.sensors.obstacle_right()]
                print(observation)
                # calculate input


                # give input
                self.game.step(input)


            #end of game loop
            self.game.count = self.game.count + 1

if __name__ == "__main__":
    b = Brain()

