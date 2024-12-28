import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # initializing pygame
    pygame.init()
    
    # create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # add classes to Groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    # create display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # initialize clock and dt
    clock = pygame.time.Clock()
    dt = 0
    
    # initialize objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    # start game loop
    while 1:
        # quit the game if x is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # set screen to black bg
        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)
        
        for object in updatable:
            object.update(dt)        
    
        for object in asteroids:
            if object.is_colliding(player):
                print("Game Over!")
                return
            for bullet in shots:
                if bullet.is_colliding(object):
                    object.split()
                    bullet.kill()
        # update screen
        pygame.display.flip()
        # pause game for 1/60 and pass passed time to dt
        dt = clock.tick(60)/1000
    
     
if __name__ == "__main__":
    main()