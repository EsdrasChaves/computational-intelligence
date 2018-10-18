import pygame
from Pacman import *
from Blinky import *
from Pinky import *
from Clyde import *
from Inky import *
from config import *
from Map import *
import numpy as np



def run(neural_net, train=False):
    pygame.init()
    win = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT),
        pygame.HWSURFACE
    )
    pygame.display.set_caption("PacMan-Game")
    mapa = Map()
    pygame.font.init()
    return game_loop(win, mapa, neural_net, train)

def calcDist(fst_point, snd_point):
        return math.hypot(fst_point[0] - snd_point[0], fst_point[1] - snd_point[1])

def game_loop(win, mapa, neural_net, train):
    pacman = Pacman(mapa, neural_net)
    blinky = Blinky(mapa, pacman)
    pinky = Pinky(mapa, pacman)
    clyde = Clyde(mapa, pacman)
    inky = Inky(mapa, pacman)
    clock = pygame.time.Clock()

    while pacman.isAlive:
        events = pygame.event.get()
        handle_quit(events)

        win.fill((0, 0, 0))

        input_data = np.array([[calcDist(pacman.getPos(), blinky.getPos()), calcDist(pacman.getPos(), pinky.getPos()), calcDist(pacman.getPos(), inky.getPos()), calcDist(pacman.getPos(), clyde.getPos())]])

        if train == False: 
            mapa.draw(win) 
        pacman.update(input_data)
        if train == False: 
            pacman.draw(win)
        blinky.update()
        if train == False: 
            blinky.draw(win)
        pinky.update()
        if train == False: 
            pinky.draw(win)
        clyde.update()
        if train == False: 
            clyde.draw(win)
        inky.update(blinky.getPos())
        if train == False: 
            inky.draw(win)

        if train == False: 
            textsurface = pygame.font.SysFont('Comic Sans MS', 25).render('Score: {}'.format(pacman.score), False, (255, 255, 255))
            win.blit(textsurface,(240,300))

        if train == False: 
            pygame.display.update()

        if train == False: 
            clock.tick(FPS)
    return (pacman.score, pacman.count2)

def handle_quit(events):
    for event in events:
        if event.type == pygame.QUIT:
            end_game()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            end_game()


def end_game():
    pygame.quit()
    exit(0)
