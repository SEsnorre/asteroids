from circleshape import CircleShape
import pygame
from constants import *
import random as r

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = r.uniform(20,50)
        v1 = pygame.Vector2(self.velocity).rotate(split_angle)
        v2 = pygame.Vector2(self.velocity).rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = v1 * 1.2
        asteroid2.velocity = v2 * 1.2