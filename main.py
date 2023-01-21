import pygame
import os
import sys
import time

from Scripts.Classes.player import Player
from Scripts.Classes.layout import Layout
from Scripts.Classes.block import Block
from Scripts.open_image import open_image
from Scripts.level_loadig import level_load
from config import cell_size, TPS, width, height


def main():
    # инициализация проекта
    pygame.init()

    # загрузка уровня
    board = Layout(cell_size, 25, 12)
    level_board = level_load("Test", "test_room", board)
    board.build(level_board)

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
