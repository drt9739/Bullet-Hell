import pygame

from Scripts.open_image import open_image

cell_size = 60


# Клетки (объекты)
class Block:
    # Инициализация
    def __init__(self, board, type_block, collision_level, sprite, global_x,
                 global_y):  # Принимает тип клетки, уровень коллизии*, спрайт (открытый файл)
        global cell_size
        self.type = type
        self.collision_level = collision_level
        self.image = open_image(sprite, 60, 60)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.image
        self.sprite.rect = self.sprite.image.get_rect()
        board.tiles.add(self.sprite)
        self.sprite.rect.x = global_x * cell_size + 210
        self.sprite.rect.y = global_y * cell_size + 150