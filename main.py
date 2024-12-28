import pygame
from constants import *

def main():
    print("Starting asteroids!")
    # initializing pygame
    (successes, failures) = pygame.init()
    #print(f"Initialized {successes} modules with {failures} failures")
    
    # create display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # start game loop
    while 1:
        # set screen to black bg
        screen.fill((0,0,0))
        
        # quit the game if x is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update screen
        pygame.display.flip()
    
    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    
if __name__ == "__main__":
    main()