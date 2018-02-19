import sys
sys.path.append('../') 
from game.game import Game

class Brain:
    def __init__(self):
        self.GAMES = 3
        self.game = Game(self.GAMES)
        self.main_loop()
        self.yo()

    def yo(self):
        print("yo")

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

