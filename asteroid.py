import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
 
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)
            vector_one = self.velocity.rotate(angle)
            vector_two = self.velocity.rotate(-angle)
            radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(self.position.x, self.position.y, radius)
            asteroid_one.velocity = vector_one * 1.2
            
            asteroid_two = Asteroid(self.position.x, self.position.y, radius)
            asteroid_two.velocity = vector_two * 1.2
            
