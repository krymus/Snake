import constants as c

class Snake:
    def __init__(self) -> None:
        self.dir = 'E'
        self.body = []
        
        self.body.append([0,2])
        self.body.append([0,3])
        self.body.append([0,4])
        self.body.append([0,5])
        self.body.append([0,6])
        self.body.append([0,7])
        self.body.append([0,8])
        self.body.append([0,9])
        self.body.append([0,10])
        self.body.append([0,11])
        self.body.append([0,12])
        self.body.append([0,13])
        self.body.append([0,14])
        self.body.append([0,15])
        self.body.append([1,15])
        self.body.append([2,15])
        self.body.append([3,15])
        self.body.append([4,15])
        self.body.append([5,15])
        self.body.append([6,15])
        self.body.append([7,15])
        self.body.append([8,15])
        self.body.append([9,15])
        self.body.append([10,15])
        self.body.append([11,15])
        self.body.append([12,15])
        self.body.append([13,15])
        self.body.append([14,15])
        self.head = self.body[-1]
        self.tail = self.body[0]
        self.size = len(self.body)



    def move(self, grow):
        if self.dir == 'N':
            self.body.append([self.head[0], (self.head[1] - 1)%c.GRID_SIZE])
        elif self.dir == 'S':
            self.body.append([self.head[0], (self.head[1] + 1)%c.GRID_SIZE])
        elif self.dir == 'E':
            self.body.append([(self.head[0] + 1)%c.GRID_SIZE, self.head[1]])
        elif self.dir == 'W':
            self.body.append([(self.head[0] - 1)%c.GRID_SIZE, self.head[1]])

        if grow == False:
            self.body.remove(self.tail)
            self.tail = self.body[0]
        else:
            self.size += 1
            
        self.head = self.body[-1]
        


    def turn(self, turn):
        if self.dir == turn or (self.dir == 'N' and turn == 'S') or (self.dir == 'S' and turn == 'N') or (self.dir == 'E' and turn == 'W') or (self.dir == 'W' and turn == 'E'):
            return
        else:
            self.dir = turn


    
        



