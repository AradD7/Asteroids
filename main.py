import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    time = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Asteroid.containers = (asteroids, updatable_group, drawable_group)
    Player.containers = (updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        updatable_group.update(dt)
        for drawing in drawable_group:
            drawing.draw(screen)
        for asteroid in asteroids:
            if asteroid.is_coliding(player):
                print("Game Over!")
                exit()
        pygame.display.flip()
        dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()