import pygame
import pacman

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FPS = 10


def run():
    pygame.init()
    win = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT),
        pygame.HWSURFACE
    )
    pygame.display.set_caption("PacMan-Game")
    game_loop(win)


def game_loop(win):
    pacman = Pacman()
    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        handle_quit(events)

        win.fill((0, 0, 0))

        pacman.update(events)
        pacman.draw(win)

        pygame.display.update()
        clock.tick(FPS)


def handle_quit(events):
    for event in events:
        if event.type == pygame.QUIT:
            end_game()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            end_game()


def end_game():
    pygame.quit()
    exit(0)


run()
