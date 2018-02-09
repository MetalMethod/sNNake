import pygame

class Controller:
     
    def detect_keyboard(self):
        if( pygame.key.get_pressed()[pygame.K_UP] == 1 ):
            return 1
        if( pygame.key.get_pressed()[pygame.K_RIGHT] == 1 ):
            return 2
        if( pygame.key.get_pressed()[pygame.K_DOWN] == 1 ):
            return 3
        if( pygame.key.get_pressed()[pygame.K_LEFT] == 1 ):
            return 4


    def update_player(self, head):
        head.checkLimits()

        if (self.detect_keyboard() == 1):
            head.up()
        if (self.detect_keyboard() == 2):
            head.right()
        if (self.detect_keyboard() == 3):
            head.down()
        if (self.detect_keyboard() == 4):
            head.left()
        return