import pygame


class Layout:
    # Инициализация
    def __init__(self, size, width, height):  # Принимает размер клетки, ширину и высоту доски в клетках
        # Работа с блоками
        self.tiles = pygame.sprite.Group()
        self.size = size
        self.width = width
        self.height = height
        self.top = 10
        self.left = 0
        # Работа с картой
        self.map = [[[[0]] * 25] * 13]
        for i in self.map:
            for j in i:
                pass

    # Установка блоков на уровень
    def build(self, pattern):
        """
        Установка блоков

        :param pattern: шаблон установки блоков+

        """
        self.map = pattern
        for i in self.map:
            for j in i:
                pass

    def render(self, screen):
        """
        Отрисовка доски

        :param screen: экран программы
        """
        self.tiles.draw(screen)
