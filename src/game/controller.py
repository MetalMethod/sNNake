import pygame

class Controller:

    def __init__(self, player):
        self.player = player

    def detect_keyboard(self):
        if (pygame.key.get_pressed()[pygame.K_UP] == 1):
            self.up()
        if (pygame.key.get_pressed()[pygame.K_RIGHT] == 1):
            self.right()
        if (pygame.key.get_pressed()[pygame.K_DOWN] == 1):
            self.down()
        if (pygame.key.get_pressed()[pygame.K_LEFT] == 1):
            self.left()
        if (pygame.key.get_pressed()[pygame.K_1] == 1):
            player.eat()
    
    def update_player(self):
        self.detect_keyboard()
        self.player.turn()
        self.player.update_body()
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
    
    def up(self):
        if (self.player.direction != 3) : self.player.direction = 1

    def right(self):
        if (self.player.direction != 4) : self.player.direction = 2

    def down(self):
        if (self.player.direction != 1) : self.player.direction = 3

    def left(self):
        if (self.player.direction != 2) : self.player.direction = 4

    def debug(self):
        print("##########################")
        for el in self.player.body_list:
            print (el.position.get_position())
        return

