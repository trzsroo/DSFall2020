import pygame
import random
from paddle import Paddle
from ball import Ball

def main():
    pygame.init()
    pygame.display.set_caption("My Pong")

    #creates a surface
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    VELOCITY = 5
    FPS = 30 #framerate

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #draw walls as rectangle
    #rect(surface, color, rect) -> Rect
    #Rect((left, top), (width, height))
    fgcolor = pygame.Color("white")
    bgcolor = pygame.Color("black")
    #top wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0),(WIDTH,BORDER)))
    #left wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0),(BORDER, HEIGHT)))
    #bottom wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))
    pygame.display.update()

    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    randNum = random.randint(0,1)
    if randNum == 1:
        vy0 = -VELOCITY
    else:
        vy0 = VELOCITY
    #todo:
    # +/- 45 degree random

    b0 = Ball(x0, y0, vx0, vy0, screen, fgcolor, bgcolor, HEIGHT, BORDER)
    b0.show(fgcolor)

    pygame.display.update() 

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)
        #Ball 
        b0.update()
                
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
