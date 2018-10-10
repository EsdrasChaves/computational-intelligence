import pygame
import math
from config import *
from Map import *



class Ghost(object):
    RADIUS = int(TILE_WIDTH/2)
    def __init__(self, mapa, color, pos_x, pos_y):
        self.mapa = mapa
        self.pos_x = pos_x 
        self.pos_y = pos_y 
        self.color = color

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

        self.handle_mov(target)

        if(self.Frame == FPS/MPS):
            self.Frame = 0;
    

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
                new_dist = math.hypot(target[0] - new_pos[0], target[1] - new_pos[1])
                if(new_dist < dist):
                    dist = new_dist
                    move = new_pos
                    new_vel = vel
        
        if self.Frame == 15:
            self.pos_x = move[0]
            self.pos_y = move[1]
            self.current_vel = new_vel

    def is_valid_move(self, vel):
        return True if ((self.mapa.map[self.pos_y + vel[1]][self.pos_x + vel[0]] != 1) and 
                        (tuple(map(sum, zip(vel, self.current_vel))) != (0, 0))) else False



