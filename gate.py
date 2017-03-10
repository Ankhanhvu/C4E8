class Gate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.text = "G "

    def print(self):
        print(self.x,self.y)

    def match(self,x,y):
        if self.x == x and self.y == y:
            return True
        else:
            return False
