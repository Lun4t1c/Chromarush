import sys
from settings import *
import pygame
from sytems.level import Level


# https://youtu.be/YWN8GcmJ-jA?t=872

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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
