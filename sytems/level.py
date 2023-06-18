import pygame
from models.tile import Tile


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_data = level_data

    def run(self):
        pass
