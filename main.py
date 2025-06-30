# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroidfield import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
from shot import *


def main():
    pygame.init()
    sat = pygame.time.Clock()
    dt = 0

    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    field = AsteroidField ()
    igrac = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for asteroid in asteroids:
            if asteroid.collides_with(igrac):
                print("Game over!")
                sys.exit()
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = sat.tick(60)/1000


if __name__ == "__main__":
    main()