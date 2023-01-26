import os
import pygame


def open_image(name, width, height, colorkey=None):  #
    if name:
        full_path = os.path.join('Data/Sprites', name)
        if os.path.isfile(full_path):
            image = pygame.image.load(full_path)
            image = pygame.transform.scale(image, (width, height))
            if colorkey is not None:
                image = image.convert()
                if colorkey == -1:
                    colorkey = image.get_at((0, 0))
                image.set_colorkey(colorkey)
            return image
    return None
