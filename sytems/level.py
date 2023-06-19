import pygame

from models.player import Player
from models.tile import Tile
from settings import *


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.setup_level(level_data)

        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if cell == 'X':
                    tile = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SCREEN_WIDTH / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed_multiplier = 0

        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed_multiplier = 0

        else:
            self.world_shift = 0
            player.speed_multiplier = 5

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()
