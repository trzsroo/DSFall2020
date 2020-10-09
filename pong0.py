import pygame

def main():
    pygame.init()
    pygame.display.set_caption("My Pong")

    #creates a surface
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #draw walls as rectangle
    #rect(surface, color, rect) -> Rect
    #Rect((left, top), (width, height))
    wcolor = pygame.Color("white")
    #top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH,BORDER)))
    #left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER, HEIGHT)))
    #bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))
    pygame.display.update()

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
