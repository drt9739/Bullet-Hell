import pygame

from Scripts.open_image import open_image
from config import cell_size


# Клетки (объекты)
class Block(pygame.sprite.Sprite):
    # Инициализация
    def __init__(self, board, type_block, sprite, global_x,
                 global_y):  # Принимает тип клетки, уровень коллизии*, спрайт (открытый файл)
        super().__init__()

        self.type = type_block
        self.image = open_image(sprite, 60, 60)
        self.rect = self.image.get_rect()
        self.rect.x = global_x * cell_size - 60
        self.rect.y = global_y * cell_size

        board.tiles.add(self)
