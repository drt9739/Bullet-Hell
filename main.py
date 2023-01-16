import pygame
import os
import sys
import time

import config
from Scripts.Class.player import Player
from Scripts.Class.layout import Layout
from Scripts.Class.block import Block
from Scripts.open_image import open_image
from config import cell_size, TPS, width, height
from Scripts.load_level import load_level


def terminate():
    pygame.quit()
    sys.exit()


class Menu:
    font_image = ''

    def __init__(self, surface: object):
        self.surface = surface

        self.run()

    def run(self):
        if self.font_image:
            font_img = open_image(self.font_image, width, height)
            screen.blit(font_img, (0, 0))

        font = pygame.font.Font(None, 30)
        text_coord = 50
        intro_text = ['говно', 'запупа']
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()
            clock.tick(config.TPS)


class Game:
    pass


def main():
    # инициализация проекта
    Menu(screen)

    board = Layout(cell_size, 25, 12)
    pattern = load_level('level.data', board)
    board.build(pattern)
    pygame.display.set_caption("It's time for bullet hell")
    size = width, height

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
    pygame.init()
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    if config.level_path == '':
        config.level_path = os.path.abspath('data')
    main()

# Примечания:
#   • Уровень коллизии - целое число, необходимое для определения возможности проникновения определённого предмета
#     через клетку (чем выше, тем сложнее)
#   • Уровень проникновение - целое число, определяющее способность предмета проходить через клетку
#   • Глобальная позиция - позиция относительно доски
#   • Локальная позиция - позиция относительно клетки
#
