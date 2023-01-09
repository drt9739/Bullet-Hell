import pygame


class Layout:
    # Инициализация
    def __init__(self, size, width, height):  # Принимает размер клетки, ширину и высоту доски в клетках
        self.tiles = pygame.sprite.Group()
        self.size = size
        self.width = width
        self.height = height
        self.top = 150
        self.left = 210
        self.map = [[[[0]] * 25] * 13]
        for i in self.map:
            for j in i:
                print(j)

    def build(self, pattern):
        self.map = pattern
        for i in self.map:
            for j in i:
                print(j)

    # Отрисовка доски (сетка времена)
    def render(self, screen):  # Принимает экран для отрисовки
        self.tiles.draw(screen)