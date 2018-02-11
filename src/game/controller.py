import pygame

class Controller:
     
    def set_player_direction(self, player):
        if (pygame.key.get_pressed()[pygame.K_UP] == 1):
            player.direction = 1
        if (pygame.key.get_pressed()[pygame.K_RIGHT] == 1):
            player.direction = 2
        if (pygame.key.get_pressed()[pygame.K_DOWN] == 1):
            player.direction = 3
        if (pygame.key.get_pressed()[pygame.K_LEFT] == 1):
            player.direction = 4
        return

    def update_player(self, player, MAP_SIZE):
        self.set_player_direction(player)
        player.move()
        player.detect_walls(MAP_SIZE)
        print(player.direction)

        if(player.alive == False): print("DEAD")


