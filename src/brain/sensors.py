
class Sensors:
    def __init__(self, grid, player):
        self.grid = grid
        self.player = player

    def detect_walls(self, grid, position_array):
        if(position_array[0] > grid.columns - 1):
            return True

        elif(position_array[0] < 0):
            return True

        elif(position_array[1] > grid.rows - 1):
            return True

        elif(position_array[1] < 0):
            return True
        else:
            return False

    def detect_body(self, position_array):
        for i in range (1, len(self.player.body_list)):
            if(position_array[0] == self.player.body_list[i].position[0] and position_array[1] == self.player.body_list[i].position[1]):
                return True

    def obstacle_forward(self):
        position_ahead = []
        if(self.player.direction == 1):
            position_ahead = [self.player.position[0], self.player.position[1] - 1 ]
        if(self.player.direction == 2):
            position_ahead = [self.player.position[0] + 1, self.player.position[1] ]
        if(self.player.direction == 3):
            position_ahead = [self.player.position[0], self.player.position[1] + 1 ]
        if(self.player.direction == 4):
            position_ahead = [self.player.position[0] - 1, self.player.position[1] ]
            
        if(self.detect_walls(self.grid, position_ahead)):
            #print("WALL AHEAD!")
            return 1

        if(self.detect_body(position_ahead)):
            #print("BODY AHEAD!")
            return 1
        return 0
    
    def obstacle_left(self):
        position_ahead_left = []
        if(self.player.direction == 1):
            position_ahead_left = [self.player.position[0] -1, self.player.position[1] ]
        if(self.player.direction == 2):
            position_ahead_left = [self.player.position[0], self.player.position[1] -1 ]
        if(self.player.direction == 3):
            position_ahead_left = [self.player.position[0] + 1, self.player.position[1] ]
        if(self.player.direction == 4):
            position_ahead_left = [self.player.position[0], self.player.position[1] + 1 ]
            
        if(self.detect_walls(self.grid, position_ahead_left)):
            #print("WALL ON LEFT!")
            return 1

        if(self.detect_body(position_ahead_left)):
            #print("BODY ON LEFT!")
            return 1
        return 0
    
    def obstacle_right(self):
        position_ahead_right = []
        if(self.player.direction == 1):
            position_ahead_right = [self.player.position[0] +1, self.player.position[1] ]
        if(self.player.direction == 2):
            position_ahead_right = [self.player.position[0], self.player.position[1] + 1 ]
        if(self.player.direction == 3):
            position_ahead_right = [self.player.position[0] - 1, self.player.position[1] ]
        if(self.player.direction == 4):
            position_ahead_right = [self.player.position[0], self.player.position[1] - 1 ]
            
        if(self.detect_walls(self.grid, position_ahead_right)):
            #print("WALL ON RIGHT!")
            return 1

        if(self.detect_body(position_ahead_right)):
            #print("BODY ON RIGHT!")
            return 1
        return 0
    

