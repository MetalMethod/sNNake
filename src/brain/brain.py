
import sys
sys.path.append('../') 
from game.game import Game
from sensors import Sensors
from random import randint

#constants
GAMES_COUNT = 3

#globals
input = 0
observation = []

class Brain:
    def __init__(self):
        self.game = Game(GAMES_COUNT)
        self.main_loop()

    def generate_action(self):
        return randint(0,4)

    # main_loop is a pool of games for training
    def main_loop(self):
        while (self.game.count <= self.game.max_games):
            #reseting game
            self.game.reset()
            self.sensors = Sensors(self.game.grid, self.game.player)    
###### reward
            self.reward = 0
            
            # game loop
            while self.game.player.alive:

                # give input to game
                direction = self.generate_action()
                self.game.step(self.sensors, direction)

                # receive  observation
                observation = [self.sensors.obstacle_forward(), self.sensors.obstacle_left(), self.sensors.obstacle_right()]
                print(observation)

###### reward
                self.reward = 1

            #end of game loop
            self.game.count = self.game.count + 1

if __name__ == "__main__":
    b = Brain()

