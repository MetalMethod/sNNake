###### first sketch of sNNake
#dependencies
import sys
import pygame

#constants
window_size = width, height = 400, 400
speed = [2, 2]

# set up the colors
BLACK = (  30,  30,  30)
WHITE = (180, 180, 180)
RED   = (100,   0,   0)
GREEN = (  0, 100,   0)
BLUE  = (  0,   0, 100)
grid_cell_size = 20

#setup
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(window_size)

#ball = pygame.image.load("ball.gif")
#ballrect = ball.get_rect()

class Player:
    x = 0
    y = 0
    speed = 10
    direction = 2

    def up(self):
        self.y = self.y - self.speed
        return

    def right(self):
        self.x = self.x + self.speed
        return
        
    def down(self):
        self.y = self.y + self.speed
        return

    def left(self):
        self.x = self.x - self.speed
        return

    def checkLimits(self):
        if(self.x > 400):
            self.x = 0

        if(self.x < 0):
            self.x = 400

        if(self.y > 400):
            self.y = 0

        if(self.y < 0):
            self.y = 400 

        return    


   
def detect_keyboard():
    if( pygame.key.get_pressed()[pygame.K_UP] == 1 ):
        return 1
    if( pygame.key.get_pressed()[pygame.K_RIGHT] == 1 ):
        return 2
    if( pygame.key.get_pressed()[pygame.K_DOWN] == 1 ):
        return 3
    if( pygame.key.get_pressed()[pygame.K_LEFT] == 1 ):
        return 4


head = Player()
head.x = window_size[0]/2
head.y = window_size[0]/2

def draw_player(head):
    pygame.draw.rect(screen, WHITE, (head.x,head.y, grid_cell_size, grid_cell_size))
    return

def update_player(head):
    head.checkLimits()

    if (detect_keyboard() == 1):
        head.up()
    if (detect_keyboard() == 2):
         head.right()
    if (detect_keyboard() == 3):
        head.down()
    if (detect_keyboard() == 4):
        head.left()
    return


#game loop
while 1:
    #msElapsed = clock.tick(30)
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    # erase the screen
    screen.fill(BLACK)

    #draw objects
    draw_player(head)
    
    #update objects
    update_player(head)

    

    #update all and close the loop
    pygame.display.update()
#close game loop
