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

        if (pygame.key.get_pressed()[pygame.K_1] == 1):
            player.eat()
        
        return

    def update_player(self, player, grid):
        self.set_player_direction(player)
        player.turn()
        player.detect_walls(grid)
        player.update_body()
       # self.debug(player)
        
    def debug(self, player):
        print("##########################")
        for el in player.body_list:
            print (el.position.get_position())
            

        #####print(len(player.body_list))
        
        ####print (player.body_list[0].info())
        ####print(player.position.get_position())
        ####print(player.direction)
        ####if(player.alive == False): print("DEAD")
        return

