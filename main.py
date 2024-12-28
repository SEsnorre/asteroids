import pygame
from constants import *
from player import *

def main():
    # initializing pygame
    pygame.init()
    
    # create display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # initialize clock and dt
    clock = pygame.time.Clock()
    dt = 0
    
    # initialize player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # start game loop
    while 1:
        # quit the game if x is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # set screen to black bg
        screen.fill("black")
        
        player.draw(screen)
        
        player.update(dt)
        # update screen
        pygame.display.flip()
        # pause game for 1/60 and pass passed time to dt
        dt = clock.tick(60)/1000
    
     
if __name__ == "__main__":
    main()