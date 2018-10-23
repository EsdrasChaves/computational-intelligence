import pygame
from config import *
from Map import *
from NeuralNetwork import *


class Pacman(object):
    RADIUS = int(TILE_WIDTH/2)
    def __init__(self, mapa, neural_net):
        self.mapa = mapa
        self.pos_x = 11
        self.pos_y = 17

        self.vel_x = 1
        self.vel_y = 0

        self.isAlive = True

        self.Frame = 0
        self.score = 0

        self.count = 0
        self.count2 = 0
        self.lastMove = ""
        self.movesCount = 0

        self.neural_network =  neural_net

    def update(self, input_data):
        self.Frame += 1

        self.handle_mov(input_data)
        self.handle_colision()

        if(self.count > TimeToStarve):
            self.killPacman()
            

        if(self.Frame == FPS/MPS):
            self.Frame = 0
        
        
    def handle_colision(self):
        if(self.mapa.map[self.pos_y][self.pos_x] == 2):
            self.mapa.getFruit(self.pos_y,self.pos_x)
            self.count = 0
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

        

    def handle_mov(self, input_data):
        movement = (self.vel_x, self.vel_y)
        vel_list = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }

        movement = vel_list[self.neural_network.nextaction(input_data)]
        if self.lastMove == movement:
            self.movesCount += 1
        else:
            self.movesCount = 0
        self.lastMove = movement


        if(self.mapa.map[self.pos_y + movement[1]][self.pos_x + movement[0]] != 1):
            self.vel_x, self.vel_y = movement
        
        if(self.Frame == (FPS/MPS) and self.mapa.map[self.pos_y + self.vel_y][self.pos_x + self.vel_x] != 1):
            self.pos_x += self.vel_x
            self.pos_y += self.vel_y
            self.count2 += 1
        
        self.count += 1

    def getPos(self):
        return (self.pos_x, self.pos_y)
    
    def getVel(self):
        return (self.vel_x, self.vel_y)
    
    def killPacman(self):
        self.isAlive = False