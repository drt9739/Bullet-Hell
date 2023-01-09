import pygame


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, screen):
        pygame.draw.circle(screen, pygame.Color("red"), (self.x, self.y), 30)

    def move(self, direction):
        velocity = 0
        if direction == "right":
            velocity = 10
        if direction == "left":
            velocity = -10
        while direction:
            self.x += velocity
            print(self.x)

    def fall(self):
        gravity_acceleration = 10
