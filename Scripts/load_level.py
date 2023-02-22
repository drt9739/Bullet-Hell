import os

from Scripts.Class.block import Block
from Scripts.Class.layout import Layout
import pygame


def load_level(file: str, board: Layout) -> tuple:
    path = os.path.abspath('data\\' + file)
    result, blocks = pygame.sprite.Group(), pygame.sprite.Group()

    with open(path) as file:
        level = file.readlines()

    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == '0':
                # Пустота
                pass
            elif level[i][j] == 'b':
                block = Block(board, 'ground', 'ground.png', j, i)
                result.add(block)
                blocks.add(block)

    return result, blocks
