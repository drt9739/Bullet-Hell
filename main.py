import os
import sys
import pygame

from pygame.locals import *
from config import *
from Scripts.open_image import open_image
from Scripts.load_level import load_level
from Scripts.Class.layout import Level
from Scripts.Class.player import Player

pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


class Menu:
    font_image = 'font.png'

    def __init__(self, scr: pygame.Surface):
        self.resolution: tuple = resolution
        self.screen: pygame.Surface = scr
        self.font: pygame.font.Font = pygame.font.Font(None, 100)

        self.texts = ['*Bullet-Hell',
                      'пока что нажми на что-нибудь чтобы начать:)']
        self.font_pos = [resolution[0] // 2, 100]
        self.font_size = 100
        self.text_coord = 10

        self.run()

    def run(self):
        background = open_image(self.font_image, *resolution)
        self.screen.blit(background, (0, 0))

        for line in self.texts:
            if '*' not in line:
                self.font = pygame.font.Font(None, 50)

            string_rendered = self.font.render(line.removeprefix('*'), True, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.x, intro_rect.y = self.font_pos[0] - intro_rect.width // 2, self.font_pos[1]
            self.font_pos[1] = self.font_pos[1] + 110
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return Game(self.screen)

            pygame.display.flip()
            clock.tick(TPS)


class Game:
    def __init__(self, scr: pygame.Surface):
        self.screen = scr
        self.wight, self.height = 30, 13
        self.block_size = 60, 60
        self.level = Level(resolution, self.block_size)
        self.blocks = self.level.get_block()

        self.players = pygame.sprite.Group()
        self.player = Player(group=self.players)
        self.screen.fill('blue')

        self.is_running = True

        self.run()

    def run(self):
        while self.is_running:
            time = clock.tick(TPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            self.player.update(time, self.blocks)
            self.screen.fill('blue')
            self.level.render(screen)
            self.players.draw(screen)

            if self.player.rect.x > resolution[0] // 2:
                self.level.next_level(screen)
                self.player.start_pos()

            pygame.display.flip()
            # for block in self.blocks:
            #     if self.player.rect.colliderect(block.rect):
            #         self.player.stop()


def main():
    Menu(screen)


if __name__ == '__main__':
    main()
