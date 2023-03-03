import pygame

from Scripts.open_image import open_image
from config import cell_size


# Клетки (объекты)
class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, size, image):  # Принимает тип клетки, спрайт (открытый файл)
        super().__init__()
        self.block_image = image
        self.image = open_image(self.block_image, size[0], size[1])
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size - size[0]
        self.rect.y = y * cell_size - size[0]


class BackgroundBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, size, image):  # Принимает тип клетки, спрайт (открытый файл)
        super().__init__()
        self.block_image = image
        self.image = open_image(self.block_image, size[0], size[1])
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size - size[0]
        self.rect.y = y * cell_size - size[0]


