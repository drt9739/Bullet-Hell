import pygame
import math

from config import BULLET_FLY_LIMIT
from Scripts.open_image import open_image


class Bullet(pygame.sprite.Sprite):
    BULLET_SIZE = 30
    BULLET_IMAGE = open_image("bullet.png", BULLET_SIZE, BULLET_SIZE)

    def __init__(self, group, x, y, speed_x, speed_y):
        super().__init__(group)

        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.speed_x = speed_x
        self.speed_y = speed_y


        self.image = Bullet.BULLET_IMAGE
        self.rect = pygame.Rect(x, y, Bullet.BULLET_SIZE, Bullet.BULLET_SIZE)

    def update(self, time: float, blocks: pygame.sprite.Group):
        fly_distance = math.sqrt(
            abs(self.start_x - self.rect.x) + abs(self.start_y - self.rect.y)
        )  # Distance between start and end
        if fly_distance > BULLET_FLY_LIMIT or pygame.sprite.spritecollideany(
            self, blocks
        ):
            self.kill()
        else:
            # pygame.Rect поддерживает только целые значения, поэтому подсчёт координат идёт в отдельных x и y
            self.x += self.speed_x * time
            self.y += self.speed_y * time
        
            self.rect.x = self.x
            self.rect.y = self.y
