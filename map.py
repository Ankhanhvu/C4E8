from player import Player
from box import Box
from gate import Gate


class Map:
    def __init__(self, width, height):
        self.player = Player(0,0)
        self.box = Box(3,4)
        self.gate = Gate(5,5)
        self.width = width
        self.height = height

    def print(self):
        for y in range(self.height):
            for x in range (self.width):
                if self.player.match (x,y):
                    print(self.player.text, end ="")
                if self.box.match (x,y):
                    print(self.box.text, end = "")
                if self.gate.match (x,y):
                    print(self.gate.text, end ="")
                else:
                    print("- ", end = "")
            print()

    def in_map(self,x,y ):
        if x < 0 or y < 0 or x > self.width - 1 or y > self.height - 1:
            return False
        return True

    def move_player(self,dx,dy):
        self.player.nextx = self.player.x + dx
        self.player.nexty = self.player.x + dy
        self.box.nextx = self.box.x + dx
        self.box.nexty = self.box.y + dy
        if self.in_map(self.player.nextx,self.player.nexty):
            if self.player.match(self.box.x,self.box.y) and self.in_map(self.box.nextx, self.box.nexty):
                self.player.move_to(self.player.nextx,self.player.nexty)
                self.box.move_to(self.box.nextx,self.box.nexty)
            elif self.player.match(self.box.x,self.box.y):
                print("try again")
            else:
                self.player.move_to(self.player.nextx, self.player.nexty)
        else:
            print("go again")

    def process_input(self, move): #direction = w.a.s.d
        direction = move.lower()
        dx = 0
        dy = 0

        if direction == "w":
            dx, dy = 0, -1
        elif direction == "s":
            dx,dy = 0, 1
        elif direction == "a":
            dx,dy = -1, 0
        elif direction == "d":
            dx,dy = 1, 0

        self.move_player(dx,dy)

    def loop(self):
        while True:
            move = input("Your move (w a s d)? ")
            self.process_input(move)
            self.print()
            if self.box.match(self.gate.x,self.gate.y):
                print("WIN")
                break




map = Map(10,10)
map.loop()
