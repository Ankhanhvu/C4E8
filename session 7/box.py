class Box:
    def __init__(self,x,y):
        self.box.x = x
        self.box.y = y
        self.text = "B "

    def print(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def match(self,x,y):
        if self.x == x and self.y == y:
            return True
        else:
            return False

    def move_to(self,x,y):
        self.x =x
        self.y =y

    def cal_next(self, dx, dy):
        return [self.x+dx, self.y +dy]


