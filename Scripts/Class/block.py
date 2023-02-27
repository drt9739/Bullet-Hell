import pygame

from Scripts.open_image import open_image
import config

# Клетки (объекты)
class Block(pygame.sprite.Sprite):
    block_image = 'block.png'

    def __init__(self, x, y, size):  # Принимает тип клетки, уровень коллизии*, спрайт (открытый файл)
        super().__init__(config.game_group_2, config.blocks_group)
        self.image = open_image(self.block_image, size[0], size[1])
        self.rect = self.image.get_rect()
        self.rect.x = x * config.CELL_SIZE - size[0]
        self.rect.y = y * config.CELL_SIZE - size[0]
    
    def draw(self, surface):
        surface.blit(
            self.image,
            self.rect
        )


class BlockUp(pygame.sprite.Sprite):
    block_image = 'block_states.png'

    def __init__(self, x, y, size):
        super().__init__()
        self.image = open_image(self.block_image, size[0], size[1] // 2)
        self.rect = self.image.get_rect()
        self.rect.x = x * config.CELL_SIZE - size[0]
        self.rect.y = y * config.CELL_SIZE


class BlockDown(Block):
    block_image = 'block_down_position.png'

    def __init__(self, x, y, size):
        super().__init__(x, y, size)
