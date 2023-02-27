import pygame
import os

from Scripts.Class.block import Block, BlockUp, BlockDown
import config


class Level:
    def __init__(self, resolution, block_size, current_level=1):
        self.resolution = resolution
        self.block_size = block_size
        self.current_level = current_level

        self.start_time = pygame.time.get_ticks()

        self.blockGroup = pygame.sprite.Group()

        self.load_level()

    def load_level(self):
        if self.current_level <= config.LEVEL_LIMIT:
            file = os.path.abspath('data\\levels\\' + f'level{self.current_level}.data')
            with open(file, 'r') as f:
                data = f.readlines()

            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[y][x] == 'b':
                        block = Block(x, y, self.block_size)
                        config.blocks_group.add(block)
                    # elif data[y][x] == 'd':
                    #     block = BlockDown(x, y, self.block_size)
                    #
                    #     self.layout.append(block)
                    # elif data[y][x] == 'u':
                    #     block = BlockUp(x, y, self.block_size)


    def render(self, screen):
        self.blockGroup.draw(screen)

    def next_level(self, screen):
        self.current_level += 1
        self.blockGroup = pygame.sprite.Group()
        self.layout = []
        self.start_time = pygame.time.get_ticks()
        self.load_level()
    
    def event_handler(self, time):
        for bullet in config.bullets_group:
            bullet.event_handler(time)
        config.game.player.event_handler(time)

    def draw(self, surface):
        surface.fill(config.BACKGROUND_COLOR)
        
        for obj in config.game_group_1:
            obj.draw(surface)
        for obj in config.game_group_2:
            obj.draw(surface)
        for obj in config.game_group_3:
            obj.draw(surface)
        for obj in config.game_group_4:
            obj.draw(surface)

        for obj in config.gui_group_1:
            obj.draw(surface)
