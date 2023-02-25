import pygame

from Scripts.open_image import open_image


class Weapon(pygame.sprite.Sprite):
    pistol_image = open_image("pistol.png", 60, 60)

    def __init__(self, width, height):
        super().__init__()

        self.image = Weapon.pistol_image
        self.rect = self.image.get_rect()
    
    def update(*args, **kwargs):
        pass
