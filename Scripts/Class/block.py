import pygame

from Scripts.open_image import open_image
from config import cell_size


# Клетки (объекты)
class Block(pygame.sprite.Sprite):
    block_image = 'ground.png'

    def __init__(self, x, y, size):  # Принимает тип клетки, уровень коллизии*, спрайт (открытый файл)
        super().__init__()
        self.image = open_image(self.block_image, size[0], size[1])
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size - size[0]
        self.rect.y = y * cell_size

