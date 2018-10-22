import pygame
import math
from config import *
from Map import *



class Ghost(object):
    RADIUS = int(TILE_WIDTH/2)
    def __init__(self, mapa, color, pos_x, pos_y, pacman):
        self.mapa = mapa
        self.pos_x = pos_x 
        self.pos_y = pos_y 
        self.color = color
        self.pacman = pacman

        self.current_vel = (0, 0)

        self.Frame = 0

        self.vel_list = {
            'right': (1, 0),
            'left': (-1, 0),
            'down': (0, 1),
            'up': (0, -1)
        }

    def update(self, target):
        self.Frame += 1

        if (((self.pos_x, self.pos_y) == self.pacman.getPos()) and self.Frame == (FPS/MPS)):
            self.pacman.killPacman()

        self.handle_mov(target)

        if (((self.pos_x, self.pos_y) == self.pacman.getPos()) and self.Frame == (FPS/MPS)):
            self.pacman.killPacman()

        if(self.Frame == FPS/MPS):
            self.Frame = 0
    

    def draw(self, win):
        pygame.draw.circle(
            win,
            pygame.color.Color(self.color),
            (
                self.pos_x * TILE_WIDTH + self.RADIUS,
                self.pos_y * TILE_HEIGHT + self.RADIUS
            ), self.RADIUS
        )

    def handle_mov(self, target):
        dist = float("inf")

        for _, vel in self.vel_list.items():
            if(self.is_valid_move(vel)):
                new_pos = (self.pos_x + vel[0], self.pos_y + vel[1])
                new_dist = self.calcDist(target, new_pos)
                if(new_dist < dist):
                    dist = new_dist
                    move = new_pos
                    new_vel = vel
        
        if self.Frame == (FPS/MPS):
            self.pos_x = move[0]
            self.pos_y = move[1]
            self.current_vel = new_vel

    def is_valid_move(self, vel):
        return True if ((self.mapa.map[self.pos_y + vel[1]][self.pos_x + vel[0]] != 1) and 
                        (tuple(map(sum, zip(vel, self.current_vel))) != (0, 0))) else False

    def calcDist(self, fst_point, snd_point):
        return math.hypot(fst_point[0] - snd_point[0], fst_point[1] - snd_point[1])

    def getPos(self):
        return (self.pos_x, self.pos_y)