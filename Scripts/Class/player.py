import pygame
import datetime

from pygame.locals import *
from Scripts.open_image import open_image


class Player(pygame.sprite.Sprite):
    player_image = open_image('player.png', 60, 60)

    def __init__(self, group, x=500, y=500):
        super().__init__(group)
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.y = 0
        self.time = datetime.datetime.now()

    def update(self, blocks):
        if pygame.key.get_pressed()[K_LEFT]:
            self.rect.x -= 4
        elif pygame.key.get_pressed()[K_RIGHT]:
            self.rect.x += 4
        elif pygame.key.get_pressed()[K_UP]:
            self.rect.y -= 4
        elif pygame.key.get_pressed()[K_DOWN]:
            self.rect.y += 4
        self.rect.y += 1

    def stop(self):
        self.rect.y -= 1

    def kill(self):
        pass

    def fall(self):
        gravity_acceleration = 10
