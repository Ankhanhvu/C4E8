class Player:
    def __init__(self,x,y): #constructor
        self.x=x
        self.y=y
        self.text = "P "

    def print(self):
        print(self.x,self.y)

    def move(self,dx,dy):
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
