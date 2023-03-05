import pygame

from pygame.locals import *
import config
from config import *
from Scripts.Class.level import Level
from Scripts.Class.button import Button

pygame.init()
screen = pygame.display.set_mode(resolution)


class Game:
    def __init__(self, surface):
        self.current_level = 0
        self.surface = surface
        self.is_running = False
        self.font_pos = (10, 10)
        self.time_pos = (10, 110)
        self.block_size = 60, 60
        self.closed_death_screen = False
        self.level = Level(resolution, self.block_size)

        self.font = get_font_for_size(100)

    def end(self):
        pass

    def launch_level(self):
        clock = pygame.time.Clock()
        self.is_running = True

        while self.is_running and config.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    config.is_running = False
                    break

            self.level.event_handler(clock.tick(TPS), self.show_death_screen)

            self.level.draw(self.surface)
            self.render_status_game()

            pygame.display.flip()

    def show_death_screen(self):
        for obj in config.game_group_1:
            obj.kill()

        for obj in config.game_group_2:
            obj.kill()

        for obj in config.game_group_3:
            obj.kill()

        for obj in config.game_group_4:
            obj.kill()

        for obj in config.gui_group_1:
            obj.kill()

        self.is_running = False
        if not self.closed_death_screen:
            EndScreen(self.surface)

    def render_status_game(self):
        line = f'Level {self.level.current_level}'
        string_rendered = self.font.render(line.removeprefix('*'), True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.x, intro_rect.y = self.font_pos[0], self.font_pos[1]
        screen.blit(string_rendered, intro_rect)

        elapsed_time = pygame.time.get_ticks() - self.level.start_time
        time_str = f"Time: {elapsed_time // 1000}.{elapsed_time % 1000:03d}"
        time_text = self.font.render(time_str, True, (255, 255, 255))
        time_rect = time_text.get_rect()
        time_rect.x, time_rect.y = self.time_pos[0], self.time_pos[1]
        screen.blit(time_text, time_rect)


class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.is_running = False

        self.title_font = get_font_for_size(44)

        self.run()

    def stop(self):
        self.is_running = False
        config.is_running = False

    def run(self):
        buttons_group = pygame.sprite.Group()
        Button(
            group=buttons_group,
            x=(self.surface.get_width() - BUTTON_SIZE_X) // 2,
            y=200,
            w=BUTTON_SIZE_X,
            h=BUTTON_SIZE_Y,
            text="Играть",
            callback=self.start_game,
        )
        Button(
            group=buttons_group,
            x=(self.surface.get_width() - BUTTON_SIZE_X) // 2,
            y=300,
            w=BUTTON_SIZE_X,
            h=BUTTON_SIZE_Y,
            text="Выйти",
            callback=self.stop,
        )

        clock = pygame.time.Clock()
        self.is_running = True

        self.surface.fill(BACKGROUND_COLOR)
        text = self.title_font.render("Bullet Hell", FONT_ANTIALIAS, WHITE)
        self.surface.blit(
            text, (40, 80)
        )

        while self.is_running and config.is_running:
            for button in buttons_group:
                button.x = 10
                button.draw(self.surface)

            events = pygame.event.get()
            events_types = {event.type for event in events}

            if pygame.QUIT in events_types:
                self.is_running = False
                config.is_running = False
                break

            for event in events:
                if event.type == pygame.VIDEORESIZE:
                    self.surface.fill(BACKGROUND_COLOR)

                    for button in buttons_group:
                        button.x = (self.surface.get_width() - button.w) // 2
                        button.draw(self.surface)

                    self.surface.blit(
                        text, ((self.surface.get_width() - text.get_width()) // 2, 80)
                    )

            for button in buttons_group:
                button.event_handler(events, events_types)

            pygame.display.flip()
            clock.tick(TPS)

    def start_game(self):
        config.game = Game(self.surface)
        config.game.launch_level()
        self.end_game()

    def end_game(self):
        config.game.end()
        config.game = None

        # Redraw text
        self.surface.fill(BACKGROUND_COLOR)
        text = self.title_font.render("Bullet Hell", FONT_ANTIALIAS, WHITE)
        self.surface.blit(
            text, ((self.surface.get_width() - text.get_width()) // 2, 120)
        )


class EndScreen:
    def __init__(self, surface):
        self.surface = surface
        self.is_running = False
        self.run()

    def run(self):
        font = get_font_for_size(44)

        self.is_running = True
        clock = pygame.time.Clock()

        buttons_group = pygame.sprite.Group()
        Button(
            group=buttons_group,
            x=(self.surface.get_width() - 600) // 2,
            y=250,
            w=600,
            h=BUTTON_SIZE_Y,
            text="Выйти в главное меню",
            callback=self.close,
        )

        self.surface.fill(BACKGROUND_COLOR)

        you_died_text = font.render("Вы прошли все уровни!", FONT_ANTIALIAS, WHITE)
        self.surface.blit(
            you_died_text,
            ((self.surface.get_width() - you_died_text.get_width()) // 2, 80),
        )

        while self.is_running and config.is_running:
            for button in buttons_group:
                button.draw(self.surface)

            events = pygame.event.get()
            events_types = {event.type for event in events}

            if pygame.QUIT in events_types:
                self.is_running = False
                config.is_running = False

            for event in events:
                if event.type == pygame.VIDEORESIZE:
                    self.surface.fill(BACKGROUND_COLOR)

                    for button in buttons_group:
                        button.x = (self.surface.get_width() - button.w) // 2
                        button.draw(self.surface)

                    self.surface.blit(
                        you_died_text,
                        (
                            (self.surface.get_width() - you_died_text.get_width()) // 2,
                            120,
                        ),
                    )

            for button in buttons_group:
                button.event_handler(events, events_types)

            pygame.display.flip()
            clock.tick(TPS)

    def close(self):
        self.is_running = False
        config.game.closed_death_screen = True


def main():
    Menu(screen)


if __name__ == '__main__':
    main()
