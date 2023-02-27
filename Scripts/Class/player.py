import time

import pygame
import datetime
import math
from time import time_ns

from pygame.locals import *
from Scripts.open_image import open_image
import config
from Scripts.Class.block import Block
from Scripts.Class.weapon import Weapon
from Scripts.Class.bullet import Bullet

TO_DEG = 180 / math.pi


def get_time_ms():
    return time_ns() // 1_000_000


class Player(pygame.sprite.Sprite):
    player_image = open_image('player.png', 60, 60)

    def __init__(self, x=0, y=960):
        super().__init__(config.game_group_3)
        self.startpos = (x, y)

        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = datetime.datetime.now()

        self.ticks_falling: int = -1
        self.ticks_jumping: int = -1

        self.delay = datetime.datetime.now().second - 2

        self.weapon = Weapon(60, 60)
        self.weapon.rect = self.rect
        self.last_shooting_time = get_time_ms()

    def event_handler(self, time: float):
        self.update_movement(time);
        self.update_weapon()
        self.handle_shooting()
    
    def draw(self, surface: pygame.Surface):
        surface.blit(
            self.image,
            self.rect
        )

        surface.blit(
            self.weapon.image,
            self.weapon.rect
        )

    def update_movement(self, time: float):
        blocks = config.blocks_group
        
        if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]:
            self.rect.x -= config.SPEED * time

            colliding_sprite = pygame.sprite.spritecollide(self, blocks, False)
            blocks_left = [block for block in colliding_sprite if self.check_left(block)]

            if blocks_left:
                self.rect.x = blocks_left[0].rect.x + blocks_left[0].rect.width
        if pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]:
            self.rect.x += config.SPEED * time

            colliding_sprite = pygame.sprite.spritecollide(self, blocks, False)
            blocks_right = [block for block in colliding_sprite if self.check_right(block)]

            if blocks_right:
                self.rect.x = blocks_right[0].rect.x - blocks_right[0].rect.width

        self.ticks_falling += 1
        self.rect.y += self.ticks_falling ** 1.4 * config.GRAVITY_ACCELERATION * time

        colliding_sprite = pygame.sprite.spritecollide(self, blocks, False)
        blocks_under = [block for block in colliding_sprite if self.check_under(block)]

        if blocks_under:
            self.ticks_falling = -1
            self.rect.y = blocks_under[0].rect.y - self.rect.height

        if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_SPACE]:
            if blocks_under:
                self.ticks_jumping = 0

        if self.ticks_jumping >= 0:
            self.ticks_jumping += 1
            self.rect.y -= (60 - self.ticks_jumping) ** 1.4 * config.GRAVITY_ACCELERATION * time

            colliding_sprite = pygame.sprite.spritecollide(self, blocks, False)
            blocks_above = [block for block in colliding_sprite if self.check_above(block)]

            if blocks_above:
                self.ticks_jumping = -1
                self.rect.y = blocks_above[0].rect.y + blocks_above[0].rect.height

            if self.ticks_jumping == 30:
                self.ticks_jumping = -1

        # if self.rect.x < 0 or self.rect.x > resolution[0]:
        #     self.rect.x = resolution[0] // 2
        #     self.rect.y = resolution[1] // 2

        # if self.rect.y < 0 or self.rect.y > resolution[1]:
        #     self.rect.x = resolution[0] // 2
        #     self.rect.y = resolution[1] // 2

    def reset(self):
        self.rect.x, self.rect.y = self.startpos
        self.delay = datetime.datetime.now().second - 2

    def check_under(self, block: Block) -> bool:
        return self.rect.y + 0.6 * self.rect.height < block.rect.y < self.rect.y + self.rect.height

    def check_above(self, block: Block) -> bool:
        return self.rect.y < block.rect.y + block.rect.height < self.rect.y + self.rect.height * 0.4

    def check_left(self, block: Block) -> bool:
        return block.rect.x + block.rect.width * 0.6 < self.rect.x < block.rect.x + block.rect.width

    def check_right(self, block: Block) -> bool:
        return block.rect.x + block.rect.width > self.rect.x + self.rect.width < block.rect.x + block.rect.width * 0.4

    def update_weapon(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        player_center_x = self.rect.x + self.rect.w / 2
        player_center_y = self.rect.y + self.rect.h / 2

        distance_x = mouse_x - player_center_x
        distance_y = mouse_y - player_center_y
        angle = math.atan2(distance_y, distance_x)  # in radians
        angle = angle * TO_DEG  # to degrees
        self.weapon.image = pygame.transform.rotate(
            pygame.transform.scale(
                Weapon.pistol_image
                if abs(angle) < 90
                else pygame.transform.flip(Weapon.pistol_image, False, True),
                (self.rect.w, self.rect.h),
            ),
            -angle,
        )

    def handle_shooting(self):
        if (
                pygame.mouse.get_pressed()[0]
                and get_time_ms() >= self.last_shooting_time + 200
        ):
            self.last_shooting_time = get_time_ms()

            mouse_x, mouse_y = pygame.mouse.get_pos()

            player_center_x = self.rect.x + Bullet.BULLET_SIZE / 2
            player_center_y = self.rect.y + Bullet.BULLET_SIZE / 2

            distance_x = (
                    mouse_x - player_center_x - Bullet.BULLET_SIZE / 2
            )
            distance_y = (
                    mouse_y - player_center_y - Bullet.BULLET_SIZE / 2
            )
            angle = math.atan2(distance_y, distance_x)

            speed_x = math.cos(angle) * config.BULLET_SPEED
            speed_y = math.sin(angle) * config.BULLET_SPEED

            if datetime.datetime.now().second - self.delay >= 2:
                Bullet(
                    player_center_x,
                    player_center_y,
                    speed_x,
                    speed_y
                )
                self.delay = datetime.datetime.now().second
