from config import *
import pygame

class Map(object):
    def __init__(self):
        with open("mapa.txt","r") as mapa:
            self.map = [list(l) for l in mapa.read().split("\n")]

        for i in self.map:
            for j in range(len(i)):
                i[j] = int(i[j])


    def draw(self, win):
        for i in range(0,28):
            for j in range(0,31):
                if(self.map[j][i] == 1):
                    pygame.draw.rect( 
                    win,
                    pygame.color.Color("white"),
                    [i*TILE_HEIGHT,
                    j*TILE_WIDTH,
                    TILE_WIDTH,
                    TILE_HEIGHT],
                    0  
                )
                if(self.map[j][i] == 2):
                    pygame.draw.circle(
                        win,
                        pygame.color.Color("red"),
                        (int((i + 0.5)*TILE_HEIGHT),
                        int((j + 0.5)*TILE_WIDTH)),
                        FOOD_SIZE
                    )
    
    def getFruit(self,x,y):
        self.map[x][y] = 0