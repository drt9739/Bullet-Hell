import pygame
import os

from Scripts.Class.block import Block, BackgroundBlock


class Level:
    def __init__(self, resolution, block_size, current_level=1):
        self.resolution = resolution
        self.block_size = block_size
        self.current_level = current_level

        self.layout = []

        self.block_group = pygame.sprite.Group()
        self.back_ground_group = pygame.sprite.Group()

        self.load_level()

    def load_level(self):
        file = os.path.abspath('data\\' + f'level{self.current_level}.data')
        with open(file, 'r') as f:
            data = f.readlines()

        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == '1':
                    block = Block(x, y, self.block_size, "block1.png")
                if data[y][x] == '2':
                    block = Block(x, y, self.block_size, "block2.png")
                if data[y][x] == '3':
                    block = Block(x, y, self.block_size, "block3.png")
                if data[y][x] == '4':
                    block = Block(x, y, self.block_size, "block4.png")
                if data[y][x] == '5':
                    block = Block(x, y, self.block_size, "block5.png")
                if data[y][x] == '6':
                    block = Block(x, y, self.block_size, "block6.png")
                if data[y][x] == '7':
                    block = Block(x, y, self.block_size, "block7.png")
                if data[y][x] == '8':
                    block = Block(x, y, self.block_size, "block8.png")
                if data[y][x] == '9':
                    block = Block(x, y, self.block_size, "block9.png")
                if data[y][x] == 't':
                    bblock = BackgroundBlock(x, y, self.block_size, "torch.png")
                    self.block_group.add(bblock)
                if data[y][x] == 'b':
                    bblock = BackgroundBlock(x, y, self.block_size, "block6.png")
                    self.block_group.add(bblock)
                if data[y][x] == 'g':
                    bblock = BackgroundBlock(x, y, self.block_size, "gold.png")
                    self.block_group.add(bblock)
                if data[y][x] == 'm':
                    bblock = BackgroundBlock(x, y, self.block_size, "target.png")
                    self.block_group.add(bblock)

                if block:
                    self.block_group.add(block)
                    self.layout.append(block)

    def render(self, screen):
        self.block_group.draw(screen)

    def next_level(self, screen):
        self.current_level += 1
        self.block_group.clear(screen, screen)

        self.load_level()

    def get_block(self):
        return self.layout


class Layout:
    # Инициализация
    def __init__(self, size, width, height):  # Принимает размер клетки, ширину и высоту доски в клетках
        self.tiles = pygame.sprite.Group()
        self.size = size
        self.width = width
        self.height = height
        self.top = 0
        self.left = 0
        self.map = [[[[0]] * 30] * 13]
        for i in self.map:
            for j in i:
                pass

    # def build(self, pattern):
    #     self.map = pattern
    #     for i in self.map:
    #         for j in i:
    #             pass

    # Отрисовка доски (сетка времена)
    def render(self, screen):  # Принимает экран для отрисовки
        self.tiles.draw(screen)
