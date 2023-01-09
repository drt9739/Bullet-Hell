import pygame
import os
import sys
import time

# Инициализация величин
gravity_acceleration = 10  # Ускорение свободного падения

cell_size = 60


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


# Класс доски
class Board:
    # Инициализация
    def __init__(self, size, width, height):  # Принимает размер клетки, ширину и высоту доски в клетках
        self.tiles = pygame.sprite.Group()
        self.size = size
        self.width = width
        self.height = height
        self.top = 150
        self.left = 210
        self.map = [[[[0]] * 25] * 13]
        for i in self.map:
            for j in i:
                print(j)

    def build(self, pattern):
        self.map = pattern
        for i in self.map:
            for j in i:
                print(j)

    # Отрисовка доски (сетка времена)
    def render(self, screen):  # Принимает экран для отрисовки
        self.tiles.draw(screen)


# Клетки (объекты)
class Tile:
    # Инициализация
    def __init__(self, board, type, collision_level, sprite, global_x,
                 global_y):  # Принимает тип клетки, уровень коллизии*, спрайт (открытый файл)
        global cell_size
        self.type = type
        self.collision_level = collision_level
        self.image = open_image(sprite, 60, 60)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.image
        self.sprite.rect = self.sprite.image.get_rect()
        board.tiles.add(self.sprite)
        self.sprite.rect.x = global_x * cell_size + 210
        self.sprite.rect.y = global_y * cell_size + 150


def open_image(name, width, height):  #
    if name:
        full_path = os.path.join('Data/sprites', name)
        if os.path.isfile(full_path):
            image = pygame.image.load(full_path)
            image = pygame.transform.scale(image, (width, height))
            return image
    return None


# главный цикл
def main():
    # инициализация проекта
    TPS = 60  # Обновления (tick) в секунду
    pygame.init()
    board = Board(cell_size, 25, 12)
    pattern = [[[[0]] * 25] * 11, [[[Tile(board, "ground", 20, "ground.png", 0, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 1, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 2, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 3, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 4, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 5, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 6, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 7, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 8, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 9, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 10, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 11, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 12, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 13, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 14, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 15, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 16, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 17, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 18, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 19, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 20, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 21, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 22, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 23, 12)],
                                    [Tile(board, "ground", 20, "ground.png", 24, 12)]]]]
    board.build(pattern)
    pygame.display.set_caption("It's time for bullet hell")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    player = Player(500, 500)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.move("right")
                if event.key == pygame.K_a:
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
