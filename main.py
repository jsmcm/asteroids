import pygame
from constants import * 
from time import sleep
from random import randrange
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    numpass, numfail = pygame.init()
    print(f"numpass: {numpass}, numfail: {numfail}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    
    Shot.containers = (updatable, drawable, shots)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # screen.fill((randrange(0,255),randrange(0,255),randrange(0,255)))
        screen.fill((0,0,0))


        for p in drawable:
            p.draw(screen)

        pygame.display.flip()
    
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                exit()
        
        for a in asteroids:
            for shot in shots:
                if a.collision(shot):
                    a.split()
                    shot.kill()
            

if __name__ == "__main__":
    main()
