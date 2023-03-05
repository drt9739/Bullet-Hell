import pygame

from Scripts.open_image import open_image
import config


# Клетки (объекты)
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, size, image):  # Принимает тип клетки, уровень коллизии*, спрайт (открытый файл)
        super().__init__(config.game_group_2, config.blocks_group)
        self.block_image = image
        self.image = open_image(self.block_image, size[0], size[1])
        self.rect = self.image.get_rect()
        self.rect.x = x * config.CELL_SIZE - size[0]
        self.rect.y = y * config.CELL_SIZE - size[0]

    def draw(self, surface):
        surface.blit(
            self.image,
            self.rect
        )


class BackgroundBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, size, image):  # Принимает тип клетки, спрайт (открытый файл)
        super().__init__(config.game_group_1)
        self.block_image = image
        self.image = open_image(self.block_image, size[0], size[1])
        self.rect = self.image.get_rect()
        self.rect.x = x * config.CELL_SIZE - size[0]
        self.rect.y = y * config.CELL_SIZE - size[0]

    def draw(self, surface):
        surface.blit(
            self.image,
            self.rect)


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, size, image):  # Принимает тип клетки, спрайт (открытый файл)
        super().__init__(config.game_group_1)
        self.block_image = image
        self.image = open_image(self.block_image, size[0], size[1])
        self.rect = self.image.get_rect()
        self.rect.x = x * config.CELL_SIZE - size[0]
        self.rect.y = y * config.CELL_SIZE - size[0]

    def draw(self, surface):
        surface.blit(
            self.image,
            self.rect
        )


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, size):  # Принимает тип клетки, спрайт (открытый файл)
        super().__init__(config.game_group_1)
        self.status = True
        self.closed = open_image(f'door_closed.png', size[0], size[1])
        self.opened = open_image(f'door_opened.png', size[0], size[1])
        self.rect = self.closed.get_rect()
        self.rect.x = x * config.CELL_SIZE - size[0]
        self.rect.y = y * config.CELL_SIZE - size[0]

    def draw(self, surface):
        if not self.status:
            surface.blit(
                self.closed,
                self.rect
            )
        else:
            surface.blit(
                self.opened,
                self.rect
            )

    def open(self):
        self.status = True
