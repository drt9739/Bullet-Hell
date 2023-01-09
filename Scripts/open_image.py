import os
import pygame


def open_image(name, width, height):  #
    if name:
        full_path = os.path.join('Data/sprites', name)
        if os.path.isfile(full_path):
            image = pygame.image.load(full_path)
            image = pygame.transform.scale(image, (width, height))
            return image
    return None
