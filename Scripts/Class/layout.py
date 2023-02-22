import pygame
import os


# class Level:
#     def __init__(self, resolution, block_size, current_level=1):
#         self.resolution = resolution
#         self.block_size = block_size
#         self.current_level = current_level
#
#         self.layout = []
#
#         self.blockGroup = pygame.sprite.Group()
#
#     def load_level(self):
#         file = os.path.abspath('data\\' + f'level{self.current_level}.data')
#         with open(file, 'r') as f:
#             data = f.readlines()
#
#         for y in data:
#             for x in data:
#
#
#     def render(self):







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
