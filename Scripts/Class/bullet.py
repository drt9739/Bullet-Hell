import pygame
import math

import config
from Scripts.open_image import open_image


class Bullet(pygame.sprite.Sprite):
    BULLET_SIZE = 30
    BULLET_IMAGE = open_image("bullet.png", BULLET_SIZE, BULLET_SIZE)

    def __init__(self, x, y, speed_x, speed_y):
        super().__init__(config.game_group_4, config.bullets_group)

        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.coll_count = 0
        self.last_block = None

        self.image = Bullet.BULLET_IMAGE
        self.rect = pygame.Rect(x, y, Bullet.BULLET_SIZE, Bullet.BULLET_SIZE)

    def event_handler(self, time: float):
        fly_distance = math.sqrt(
            abs(self.start_x - self.rect.x) + abs(self.start_y - self.rect.y)
        )  # Расстояние от начала полёта до конца полёта
        if fly_distance > config.BULLET_FLY_LIMIT or self.coll_count >= 3:
            self.kill()
        else:
            for block in config.blocks_group:
                block_rect = block.rect
                bullet_rect = self.rect
                if self.rect.colliderect(block.rect) and self.last_block != block:
                    if block_rect.collidepoint(bullet_rect.midleft):
                        self.speed_x = -self.speed_x
                    elif block_rect.collidepoint(bullet_rect.midright):
                        self.speed_x = -self.speed_x
                    elif block_rect.collidepoint(bullet_rect.midtop):
                        self.speed_y = -self.speed_y
                    elif block_rect.collidepoint(bullet_rect.midbottom):
                        self.speed_y = -self.speed_y

                    elif block.rect.colliderect(bullet_rect):
                        self.speed_y = -self.speed_y
                        self.speed_x = -self.speed_x

                    self.coll_count += 1
                    self.last_block = block
                # print(self.rect.colliderect(block.rect))

            # pygame.Rect поддерживает только целые значения, поэтому подсчёт координат идёт в отдельных x и y
            self.x += self.speed_x * time
            self.y += self.speed_y * time

            self.rect.x = self.x
            self.rect.y = self.y
    
    def draw(self, surface):
        print ("Drawing")
        surface.blit(
            self.image,
            self.rect
        )
