import constants as c

class Snake:
    def __init__(self) -> None:
        self.size = 0

    def grow(self, field):
        if not self.body:
            self.tail = field
        self.body.append(field)
        self.head = field
        size += 1

    def move(self, dir):
        self.body.remove(self.tail)
        if dir == 'N':
            self.body.append()
        

