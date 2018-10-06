from config import *
import pygame

class Map(object):
    def __init__(self):
        with open("mapa.txt","r") as mapa:
            self.map = mapa.read().split("\n")

    def draw(self, win):
        for i in range(0,28):
            for j in range(0,31):
                if(self.map[j][i] == '1'):
                    pygame.draw.rect( 
                    win,
                    pygame.color.Color("white"),
                    [i*HEIGHT_IN_TILES,
                    j*WIDTH_IN_TILES,
                    WIDTH_IN_TILES,
                    HEIGHT_IN_TILES],
                    0  
                )