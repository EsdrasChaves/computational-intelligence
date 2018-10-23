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

        up = 0
        down = 0
        left = 0
        right = 0

        pac_bli_x = pacman.getPos()[0] - blinky.getPos()[0]
        pac_bli_y = pacman.getPos()[1] - blinky.getPos()[1]
        pac_pin_x = pacman.getPos()[0] - pinky.getPos()[0]
        pac_pin_y = pacman.getPos()[1] - pinky.getPos()[1]
        pac_ink_x = pacman.getPos()[0] - inky.getPos()[0]
        pac_ink_y = pacman.getPos()[1] - inky.getPos()[1]
        pac_cly_x = pacman.getPos()[0] - clyde.getPos()[0]
        pac_cly_y = pacman.getPos()[1] - clyde.getPos()[1]

        input_data = np.array([[pac_bli_x, pac_bli_y, pac_cly_x, pac_cly_y, pac_ink_x, pac_ink_y, pac_pin_x, pac_pin_y]])
        
        np.interp(input_data, (-26, 26), (-1, +1))

        if(mapa.map[pacman.getPos()[1] - 1][pacman.getPos()[0]] != 1):
            up = 1
        if(mapa.map[pacman.getPos()[1] + 1][pacman.getPos()[0]] != 1):
            down = 1
        if(mapa.map[pacman.getPos()[1]][pacman.getPos()[0] + 1] != 1):
            right = 1
        if(mapa.map[pacman.getPos()[1]][pacman.getPos()[0] - 1] != 1):
            left = 1
        
        input_data = np.append(np.array([[up, right, down, left]]), input_data, axis=1)

        pacman.update(input_data)
        blinky.update()
        pinky.update()
        clyde.update()
        inky.update(blinky.getPos())

        if train == False: 
            mapa.draw(win) 
            pacman.draw(win)
            blinky.draw(win)
            pinky.draw(win)
            clyde.draw(win)
            inky.draw(win)
            textsurface = pygame.font.SysFont('Comic Sans MS', 25).render('Score: {}'.format(pacman.score), False, (255, 255, 255))
            win.blit(textsurface,(240,300))
            pygame.display.update()
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
