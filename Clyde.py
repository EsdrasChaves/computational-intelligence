from Ghost import *

### Clyde behavior -- Tries to go to Pacman's position if he's not closer than 8 tiles, otherwise he 
###                   runs away to tile (1, 31) ###


class Clyde(Ghost):
    def __init__(self, mapa):
        Ghost.__init__(self, mapa, "orange", 1, 29)

    def update(self, pacman_pos):
        if (Ghost.calcDist(self, (self.pos_x, self.pos_y), pacman_pos) < 8):
            target = (1, 31)
        else:
            target = pacman_pos
        Ghost.update(self, target)