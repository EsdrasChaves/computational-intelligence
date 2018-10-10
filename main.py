import pygame
from Pacman import *
from Blinky import *
from Pinky import *
from config import *
from Map import *



def run():
    pygame.init()
    win = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT),
        pygame.HWSURFACE
    )
    pygame.display.set_caption("PacMan-Game")
    mapa = Map()

    game_loop(win, mapa)



def game_loop(win, mapa):
    pacman = Pacman(mapa)
    blinky = Blinky(mapa)
    pinky = Pinky(mapa)
    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        handle_quit(events)

        win.fill((0, 0, 0))

        mapa.draw(win)
        pacman.update(events)
        pacman.draw(win)
        blinky.update(pacman.getPos())
        blinky.draw(win)
        pinky.update(pacman.getPos(), pacman.getVel())
        pinky.draw(win)

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
