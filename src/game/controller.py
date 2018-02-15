import pygame

class Controller:
    
    def detect_keyboard(self, player):
        if (pygame.key.get_pressed()[pygame.K_UP] == 1):
            self.up(player)
        if (pygame.key.get_pressed()[pygame.K_RIGHT] == 1):
            self.right(player)
        if (pygame.key.get_pressed()[pygame.K_DOWN] == 1):
            self.down(player)
        if (pygame.key.get_pressed()[pygame.K_LEFT] == 1):
            self.left(player)
        if (pygame.key.get_pressed()[pygame.K_1] == 1):
            player.eat()
    
    def update_player(self, player):
        self.detect_keyboard(player)
        player.turn()
        player.update_body()
        #self.debug(player)

    def up(self, player):
        if (player.direction != 3) : player.direction = 1

    def right(self, player):
        if (player.direction != 4) : player.direction = 2

    def down(self, player):
        if (player.direction != 1) : player.direction = 3

    def left(self, player):
        if (player.direction != 2) : player.direction = 4


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

