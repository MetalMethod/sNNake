
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
        return randint(-1,1)

    def get_reward(self):
        if(self.game.player.alive): reward = 0
        else: reward = -1
        if(self.game.player.food): reward = 1
        return reward

    def init_distance(self):
        self.previous_distance_x = 0
        self.previous_distance_y = 0

    def get_food_distance(self):
        distance_x = (self.game.player.position[0] - self.game.food.position[0]) 
        distance_y = self.game.player.position[1] - self.game.food.position[1]

        if(distance_x < 0): distance_x = distance_x * -1
        if(distance_y < 0): distance_y = distance_y * -1

        result = -1
                
        if(distance_x < self.previous_distance_x):
            result = 1

        if(distance_y < self.previous_distance_y):
            result = 1
         
        self.previous_distance_x = distance_x
        self.previous_distance_y = distance_y
        print("   ", result)
        return result


    # main_loop is a pool of games for training
    def main_loop(self):
        while (self.game.count <= self.game.max_games):
            #reseting game
            self.game.reset()
            
            self.init_distance()

            self.sensors = Sensors(self.game.grid, self.game.player)    

            # game loop
            while self.game.player.alive:

                # give input to game
                action = self.generate_action()
                #action = 0
                self.game.step(self.sensors, action)
##########
                self.get_food_distance()
                print(self.get_food_distance())
##########
                # get observation
                observation = [self.sensors.obstacle_forward(), self.sensors.obstacle_left(), self.sensors.obstacle_right(), self.get_food_distance(), action, self.get_reward()]
                #print("forward ",self.sensors.obstacle_forward(), "    left ", self.sensors.obstacle_left(),"    right ", self.sensors.obstacle_right(), "    food ", self.get_food_distance(), "    action ", action, "   reward ", self.get_reward())
                #print(observation)

            #end of game loop
            self.game.count = self.game.count + 1

if __name__ == "__main__":
    b = Brain()

