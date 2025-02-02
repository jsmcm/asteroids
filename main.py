import pygame
from constants import * 
from time import sleep
from random import randrange

def main():

    numpass, numfail = pygame.init()
    print(f"numpass: {numpass}, numfail: {numfail}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
