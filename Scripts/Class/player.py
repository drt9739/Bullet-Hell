import pygame
import datetime

from pygame.locals import *
from Scripts.open_image import open_image


class Player(pygame.sprite.Sprite):
    # Инициализация
    player_image = open_image('player.png', 60, 60)
    def __init__(self, *group, x=500, y=500, penetration_level=1):
        super().__init__(*group)
        # Базовая конфигурация игрока
        self.time = datetime.datetime.now() # (Возможно пригодится для падения)
        self.penetration_level = penetration_level

        # Работа со спрайтом
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.y = 0


    def update(self):
        """
        Движение
        """
        if pygame.key.get_pressed()[K_LEFT]: # Влево
            self.rect.x -= 3
        elif pygame.key.get_pressed()[K_RIGHT]: # Вправо
            self.rect.x += 3
        elif pygame.key.get_pressed()[K_UP]: # Вверх
            self.rect.y -= 3
        elif pygame.key.get_pressed()[K_DOWN]: # Вниз
            self.rect.y += 3
        # self.rect.y += 1

    def kill(self):
        """
        Убийство
        """
        pass

    def fall(self):
        """
        Падение игрока
        """
        gravity_acceleration = 10

    # Стрельба игрока
    def shoot(self, weapon):
        """
        Стрельба

        :param weapon: оружие игрока (сам объект)
        """
        # weapon.shoot(<направление>)
        pass