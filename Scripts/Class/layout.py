import pygame
import os

from Scripts.Class.block import Block, BlockUp, BlockDown
from config import LEVEL_LIMIT


class Level:
    def __init__(self, resolution, block_size, current_level=1):
        self.resolution = resolution
        self.block_size = block_size
        self.current_level = current_level

        self.start_time = pygame.time.get_ticks()
        self.layout = []

        self.blockGroup = pygame.sprite.Group()

        self.load_level()

    def load_level(self):
        if self.current_level <= LEVEL_LIMIT:
            file = os.path.abspath('data\\levels\\' + f'level{self.current_level}.data')
            with open(file, 'r') as f:
                data = f.readlines()

            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[y][x] == 'b':
                        block = Block(x, y, self.block_size)
                        self.blockGroup.add(block)
                        self.layout.append(block)
                    # elif data[y][x] == 'd':
                    #     block = BlockDown(x, y, self.block_size)
                    #
                    #     self.layout.append(block)
                    # elif data[y][x] == 'u':
                    #     block = BlockUp(x, y, self.block_size)

                        self.layout.append(block)

    def render(self, screen):
        self.blockGroup.draw(screen)

    def next_level(self, screen):
        self.current_level += 1
        self.blockGroup = pygame.sprite.Group()
        self.layout = []
        self.start_time = pygame.time.get_ticks()
        self.load_level()

    def get_block(self):
        return self.layout
