class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 2

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