import sys
from settings import *
import pygame
from systems.level import Level


# https://youtu.be/wJMDh9QGRgs?t=48

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(example_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    level.run()

    pygame.display.update()
    clock.tick(60)
