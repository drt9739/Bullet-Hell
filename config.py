import pygame

from time import time_ns

CELL_SIZE = 60
GRAVITY_ACCELERATION = 0.004
TPS = 120  # Обновления (tick) в секунду
resolution = width, height = 1920, 1080
level_path = ''
SPEED = 0.7
BULLET_SPEED = 2
BULLET_FLY_LIMIT = 100
LEVEL_LIMIT = 15

FONT_ANTIALIAS = True

# Colors
WHITE = pygame.color.Color("#fAf8FF")
PLAYER_COLOR = pygame.color.Color("#3745F5")
BACKGROUND_COLOR = pygame.color.Color("#1E2331")
HUD_COLOR = pygame.color.Color("#272E40")

BUTTON_COLOR = pygame.color.Color("#33505D")
BUTTON_HOVER_COLOR = pygame.color.Color("#51827B")
BUTTON_SIZE_X, BUTTON_SIZE_Y = 400, 60


def get_time_ms():
    return time_ns() // 1_000_000


_fonts = {}
def get_font_for_size(size: int) -> pygame.font.Font:
    if size in _fonts:
        return _fonts[size]
    
    font = pygame.font.SysFont("Roboto", size)
    _fonts[size] = font

    return font

game = None
is_running = True

# Sprite groups
game_group_1 = pygame.sprite.Group()  # Lowest
game_group_2 = pygame.sprite.Group()
game_group_3 = pygame.sprite.Group()
game_group_4 = pygame.sprite.Group()  # Highest

gui_group_1 = pygame.sprite.Group()  # Lowest
gui_group_2 = pygame.sprite.Group()
gui_group_3 = pygame.sprite.Group()  # Highest

gui_group_custom = pygame.sprite.Group()

blocks_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
