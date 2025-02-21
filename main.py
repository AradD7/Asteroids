import pygame
from constants import *
from player import *

def main():
    pygame.init()
    time = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        updatable_group.update(dt)
        for drawing in drawable_group:
            drawing.draw(screen)
        pygame.display.flip()
        dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()