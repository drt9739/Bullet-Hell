import pygame
import os

from Scripts.Class.block import Block, BackgroundBlock, Target, Door
from Scripts.Class.player import Player
import config


class Level:
    def __init__(self, resolution, block_size, current_level=1):
        self.resolution = resolution
        self.block_size = block_size
        self.current_level = current_level
        self.player = Player()
        self.targets = []
        self.door = []
        self.start_time = pygame.time.get_ticks()

        self.load_level()

    def load_level(self):
        if self.current_level <= config.LEVEL_LIMIT:
            file = os.path.abspath('data\\levels\\' + f'level{self.current_level}.data')
            with open(file, 'r') as f:
                data = f.readlines()

            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[y][x] == '1':
                        Block(x, y, self.block_size, "block1.png")
                    elif data[y][x] == '2':
                        Block(x, y, self.block_size, "block2.png")
                    elif data[y][x] == '3':
                        Block(x, y, self.block_size, "block3.png")
                    elif data[y][x] == '4':
                        Block(x, y, self.block_size, "block4.png")
                    elif data[y][x] == '5':
                        Block(x, y, self.block_size, "block5.png")
                    elif data[y][x] == '6':
                        Block(x, y, self.block_size, "block6.png")
                    elif data[y][x] == '7':
                        Block(x, y, self.block_size, "block7.png")
                    elif data[y][x] == '8':
                        Block(x, y, self.block_size, "block8.png")
                    elif data[y][x] == '9':
                        Block(x, y, self.block_size, "block9.png")
                    elif data[y][x] == 't':
                        BackgroundBlock(x, y, self.block_size, "torch.png")
                    elif data[y][x] == 'b':
                        BackgroundBlock(x, y, self.block_size, "block6.png")
                    elif data[y][x] == 'g':
                        BackgroundBlock(x, y, self.block_size, "gold.png")
                    elif data[y][x] == 'm':
                        target = Target(x, y, self.block_size, "target.png")
                        self.targets.append(target)
                    elif data[y][x] == 'd':
                        door = Door(x, y, self.block_size)
                        config.door = door

    def next_level(self):
        self.current_level += 1
        self.start_time = pygame.time.get_ticks()

        # удаление всех игровых объектов из всех групп
        for obj in config.game_group_1:
            obj.kill()
        for obj in config.game_group_2:
            obj.kill()
        for obj in config.game_group_3:
            obj.kill()
        for obj in config.game_group_4:
            obj.kill()

        self.player = Player()

        self.load_level()

    def event_handler(self, time, callback):
        for bullet in config.bullets_group:
            bullet.event_handler(time, self.targets)

        self.player.event_handler(time)
        if config.door:
            if config.door.status and self.player.rect.colliderect(config.door.rect):
                self.next_level()
            if self.current_level == 3:
                callback()

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
