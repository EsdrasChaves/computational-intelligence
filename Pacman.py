import pygame
from config import *
from Map import *



class Pacman(object):
    RADIUS = int(TILE_WIDTH/2)
    def __init__(self, mapa):
        self.mapa = mapa
        self.pos_x = 1 
        self.pos_y = 1 

        self.vel_x = 1
        self.vel_y = 0

        self.Frame = 0
        self.score = 0

    def update(self, events):
        self.Frame += 1

        self.handle_mov(events)
        self.handle_colision()

        if(self.Frame == FPS/MPS):
            self.Frame = 0;
    
    def handle_colision(self):
        if(self.mapa.map[self.pos_y][self.pos_x] == 2):
            self.mapa.getFruit(self.pos_y,self.pos_x)
            self.score += 1


    def draw(self, win):
        pygame.draw.circle(
            win,
            pygame.color.Color("yellow"),
            (
                self.pos_x * TILE_WIDTH + self.RADIUS,
                self.pos_y * TILE_HEIGHT + self.RADIUS
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

        
        if(self.mapa.map[self.pos_y + movement[1]][self.pos_x + movement[0]] != 1):
            self.vel_x, self.vel_y = movement
            
        if(self.Frame == 15 and self.mapa.map[self.pos_y + self.vel_y][self.pos_x + self.vel_x] != 1):
            self.pos_x += self.vel_x
            self.pos_y += self.vel_y


    def getPos(self):
        return (self.pos_x, self.pos_y)
    
    def getVel(self):
        return (self.vel_x, self.vel_y)
