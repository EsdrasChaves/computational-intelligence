import pygame
from Pacman import *
from Blinky import *
from Pinky import *
from Clyde import *
from Inky import *
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
    pygame.font.init()
    game_loop(win, mapa)



def game_loop(win, mapa):
    pacman = Pacman(mapa)
    blinky = Blinky(mapa, pacman)
    pinky = Pinky(mapa, pacman)
    clyde = Clyde(mapa, pacman)
    inky = Inky(mapa, pacman)
    clock = pygame.time.Clock()

    while pacman.isAlive:
        events = pygame.event.get()
        handle_quit(events)

        win.fill((0, 0, 0))

        mapa.draw(win)
        pacman.update(events)
        pacman.draw(win)
        blinky.update()
        blinky.draw(win)
        pinky.update()
        pinky.draw(win)
        clyde.update()
        clyde.draw(win)
        inky.update(blinky.getPos())
        inky.draw(win)

        textsurface = pygame.font.SysFont('Comic Sans MS', 25).render('Score: {}'.format(pacman.score), False, (255, 255, 255))
        win.blit(textsurface,(240,300))

        pygame.display.update()

        clock.tick(FPS)
    input()

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
