import pygame
from config import *
from Map import *



class Pacman(object):
    RADIUS = int(WIDTH_IN_TILES/2)

    def __init__(self, mapa):
        self.mapa = mapa
        self.pos_x = 1 
        self.pos_y = 1 

        self.vel_x = 1
        self.vel_y = 0

    def update(self, events):
        self.handle_mov(events)

    def draw(self, win):
        pygame.draw.circle(
            win,
            pygame.color.Color("yellow"),
            (
                self.pos_x * WIDTH_IN_TILES + self.RADIUS,
                self.pos_y * HEIGHT_IN_TILES + self.RADIUS
            ), self.RADIUS
        )

    def handle_mov(self, events):
        movement = (self.vel_x, self.vel_y)
        vel_list = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    movement = vel_list['up']
                elif event.key == pygame.K_DOWN:
                    movement = vel_list['down']
                elif event.key == pygame.K_LEFT:
                    movement = vel_list['left']
                elif event.key == pygame.K_RIGHT:
                    movement = vel_list['right']


        if(self.mapa.map[self.pos_y + movement[1]][self.pos_x + movement[0]] != '1'):
            self.vel_x, self.vel_y = movement
            
        if(self.mapa.map[self.pos_y + self.vel_y][self.pos_x + self.vel_x] != '1'):
            self.pos_x += self.vel_x
            self.pos_y += self.vel_y

    def check_borders(self):
        if self.pos_x > WIDTH_IN_TILES - 1 or self.pos_x <= 0:
            end_game()
        elif self.pos_y > HEIGHT_IN_TILES - 1 or self.pos_y <= 0:
            end_game()


