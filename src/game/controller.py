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

    # def input_api(self, player, input_value):
    #     if (input_value == 1)
    #         self.up(player)
    #     if (input_value == 2)
    #         self.right(player)
    #     if (input_value == 3)
    #         self.down(player)
    #     if (input_value == 4)
    #         self.left(player)
    
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
        return

