import sys
sys.path.append('../') 
from game.game import Game

g = Game(3)
print(g.observation())