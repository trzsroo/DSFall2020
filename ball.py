import pygame

class Ball:
    # pass

    #class variables
    RADIUS = 10

    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor, height, border):
        #instance variables
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        # self.width = width # might use later
        self.height = height
        self.border = border

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        #np = od + dp
        #delete old ball
        self.show(self.bgcolor)
        if self.x == (self.border + self.RADIUS):
            self.vx = -self.vx
        if self.y == (self.border + self.RADIUS) or self.y == (self.height - (self.border + self.RADIUS)):
            self.vy = -self.vy
        self.x = self.x + self.vx
        self.y = self.y + self.vy 
        self.show(self.fgcolor)
        #todo:
        #Check if collided (wall position):
            #flip the velocity
