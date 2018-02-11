import pygame

class Controller:
     
    def set_player_direction(self, player):
        if (pygame.key.get_pressed()[pygame.K_UP] == 1 and player.direction != 3):
            player.direction = 1
        if (pygame.key.get_pressed()[pygame.K_RIGHT] == 1 and player.direction != 4):
            player.direction = 2
        if (pygame.key.get_pressed()[pygame.K_DOWN] == 1 and player.direction != 1):
            player.direction = 3
        if (pygame.key.get_pressed()[pygame.K_LEFT] == 1 and player.direction != 2):
            player.direction = 4
        return

    def update_player(self, player, grid):
        self.set_player_direction(player)
        player.move()
        player.detect_walls(grid)
        
    def debug(self, player):
        #print(player.direction)
        #if(player.alive == False): print("DEAD")
        return

