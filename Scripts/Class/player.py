import pygame
import datetime

from pygame.locals import *
from Scripts.open_image import open_image
from config import SPEED, gravity_acceleration
from Scripts.Class.block import Block


class Player(pygame.sprite.Sprite):
    player_image = open_image('player.png', 60, 60)

    def __init__(self, group, x=0, y=960):
        super().__init__(group)
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = datetime.datetime.now()

        self.ticks_falling: int = -1
        self.ticks_jumping: int = -1

    def update(self, time: float, blocks: pygame.sprite.Group):
        if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]:
            self.rect.x -= SPEED * time
            
            colliding_sprite = pygame.sprite.spritecollide(self, blocks, False)
            blocks_left = [block for block in colliding_sprite if self.check_left(block)]

            if blocks_left:
                self.rect.x = blocks_left[0].rect.x + blocks_left[0].rect.width
        if pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]:
            self.rect.x += SPEED * time

            colliding_sprite = pygame.sprite.spritecollide(self, blocks, False)
            blocks_right = [block for block in colliding_sprite if self.check_right(block)]

            if blocks_right:
                self.rect.x = blocks_right[0].rect.x - blocks_right[0].rect.width
        
        self.ticks_falling += 1
        self.rect.y += self.ticks_falling ** 1.4 * gravity_acceleration * time

        colliding_sprite = pygame.sprite.spritecollide(self, blocks, False)
        blocks_under = [block for block in colliding_sprite if self.check_under(block)]

        if blocks_under:
            self.ticks_falling = -1;
            self.rect.y = blocks_under[0].rect.y - self.rect.height

        if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_SPACE]:
            if blocks_under:
                self.ticks_jumping = 0
        
        if self.ticks_jumping >= 0:
            self.ticks_jumping += 1
            self.rect.y -= (60 - self.ticks_jumping) ** 1.4 * gravity_acceleration * time

            colliding_sprite = pygame.sprite.spritecollide(self, blocks, False)
            blocks_above = [block for block in colliding_sprite if self.check_above(block)]

            if blocks_above:
                self.ticks_jumping = -1;
                self.rect.y = blocks_above[0].rect.y + blocks_above[0].rect.height 
            
            if self.ticks_jumping == 30:
                self.ticks_jumping = -1
    
    def check_under(self, block: Block) -> bool:
        return self.rect.y + 0.6 * self.rect.height < block.rect.y < self.rect.y + self.rect.height

    def check_above(self, block: Block) -> bool:
        return self.rect.y < block.rect.y + block.rect.height < self.rect.y + self.rect.height * 0.4
    
    def check_left(self, block: Block) -> bool:
        return block.rect.x + block.rect.width * 0.6 < self.rect.x < block.rect.x + block.rect.width
    
    def check_right(self, block: Block) -> bool:
        return block.rect.x + block.rect.width > self.rect.x + self.rect.width < block.rect.x + block.rect.width * 0.4