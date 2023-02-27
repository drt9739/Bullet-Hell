import pygame

from Scripts.open_image import open_image


class Target(pygame.sprite.Sprite):
    image = 'target.png'

    def __init__(self, x, y, size):
        image = open_image(self.image, size, size)

