import pygame

pygame.init()
screen = pygame.display.set_mode([800,600])

done = False

#draw background
COLOR_WHITE = (255,255,255) #tubal, hang so k thay doi dc
player_image = pygame.image.load("mario.png")
square_image = pygame.image.load("square.png")
box_image = pygame.image.load("box.png")
x = 100
y = 100
SQUARE_SIZE = 32

class Player:
    def __init__(self,x,y): #constructor
        self.x = x
        self.y = y

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def match(self,x,y):
        if self.x == x and self.y ==y:
            return True
        else:
            return False

    def cal_next_position(self, dx, dy):
        return [self.x + dx, self.y + dy]


class Box:
    def __init__(self, x, y):  # constructor
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def match(self, x, y):
        if self.x == x and self.y == y:
            return True
        else:
            return False

    def cal_next_position(self, dx, dy):
        return [self.x + dx, self.y + dy]

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(1, 1)
        self.box = Box(5, 5)

    def move_player(self, dx, dy):
        [next_player_x, next_player_y] = self.player.cal_next_position(dx, dy)
        [next_box_x, next_box_y] = self.box.cal_next_position(dx, dy)
        if self.check_inside(next_player_x, next_player_y):
            if self.player.match(next_box_x, next_box_y) and self.check_inside(next_box_x, next_box_y):
                self.player.move(dx, dy)
                self.box.move(dx,dy)
            else:
                self.player.move(dx, dy)
        else:
            print('Go again')

    def check_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

map = Map(10, 10)

#draw image

while not done:
    key_arrow = None
    dx,dy = 0,0
    #get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1


    #process game events

    if dx != 0 or dy != 0:
        map.move_player(dx,dy)

    #repaint
    screen.fill(COLOR_WHITE)
    for y in range(map.height):
        for x in range (map.width):
            screen.blit(square_image,(x * SQUARE_SIZE, y * SQUARE_SIZE))

    screen.blit(player_image, (map.player.x * SQUARE_SIZE, map.player.y * SQUARE_SIZE))
    screen.blit(box_image, (map.box.x * SQUARE_SIZE, map.box.y * SQUARE_SIZE))
    pygame.display.flip()
