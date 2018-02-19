import sys
sys.path.append('../') 
from game.game import Game

#constants
GAMES = 3

class Brain:
    def __init__(self):
        self.game = Game(GAMES)
        self.main_loop()

    def main_loop(self):
        while (self.game.game_count <= self.game.max_games):
            self.game.game_status()
            self.game.init_game_objects()
            self.game.score = 0
            self.game.game_loop()
            self.game.game_count = self.game.game_count + 1
            print(self.game.observation())






if __name__ == "__main__":
    b = Brain()

