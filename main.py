import pygame
import os
import sys
import time

from Scripts.Class.player import Player
from Scripts.Class.layout import Layout
from Scripts.Class.block import Block
from Scripts.open_image import open_image
from config import cell_size, TPS, width, height


def main():
    # инициализация проекта
    pygame.init()
    board = Layout(cell_size, 25, 12)
    pattern = [[[[0]] * 25] * 11, [[[Block(board, "ground", 20, "ground.png", 0, 12)],
                                    [Block(board, "ground", 20, "ground.png", 1, 12)],
                                    [Block(board, "ground", 20, "ground.png", 2, 12)],
                                    [Block(board, "ground", 20, "ground.png", 3, 12)],
                                    [Block(board, "ground", 20, "ground.png", 4, 12)],
                                    [Block(board, "ground", 20, "ground.png", 5, 12)],
                                    [Block(board, "ground", 20, "ground.png", 6, 12)],
                                    [Block(board, "ground", 20, "ground.png", 7, 12)],
                                    [Block(board, "ground", 20, "ground.png", 8, 12)],
                                    [Block(board, "ground", 20, "ground.png", 9, 12)],
                                    [Block(board, "ground", 20, "ground.png", 10, 12)],
                                    [Block(board, "ground", 20, "ground.png", 11, 12)],
                                    [Block(board, "ground", 20, "ground.png", 12, 12)],
                                    [Block(board, "ground", 20, "ground.png", 13, 12)],
                                    [Block(board, "ground", 20, "ground.png", 14, 12)],
                                    [Block(board, "ground", 20, "ground.png", 15, 12)],
                                    [Block(board, "ground", 20, "ground.png", 16, 12)],
                                    [Block(board, "ground", 20, "ground.png", 17, 12)],
                                    [Block(board, "ground", 20, "ground.png", 18, 12)],
                                    [Block(board, "ground", 20, "ground.png", 19, 12)],
                                    [Block(board, "ground", 20, "ground.png", 20, 12)],
                                    [Block(board, "ground", 20, "ground.png", 21, 12)],
                                    [Block(board, "ground", 20, "ground.png", 22, 12)],
                                    [Block(board, "ground", 20, "ground.png", 23, 12)],
                                    [Block(board, "ground", 20, "ground.png", 24, 12)]]]]
    board.build(pattern)
    pygame.display.set_caption("It's time for bullet hell")
    size = width, height
    screen = pygame.display.set_mode(size)
    player = Player(500, 500)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move("right")
                if event.key == pygame.K_LEFT:
                    player.move("left")
        pygame.time.Clock()
        screen.fill(pygame.Color("white"))
        board.render(screen)
        player.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()

# Примечания:
#   • Уровень коллизии - целое число, необходимое для определения возможности проникновения определённого предмета
#     через клетку (чем выше, тем сложнее)
#   • Уровень проникновение - целое число, определяющее способность предмета проходить через клетку
#   • Глобальная позиция - позиция относительно доски
#   • Локальная позиция - позиция относительно клетки
#
