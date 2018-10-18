from Ghost import *

### Clyde behavior -- Tries to go to Pacman's position if he's not closer than 8 tiles, otherwise he 
###                   runs away to tile (1, 31) ###


class Clyde(Ghost):
    def __init__(self, mapa, pacman):
        Ghost.__init__(self, mapa, "orange", 26, 26, pacman)

    def update(self):
        if (Ghost.calcDist(self, (self.pos_x, self.pos_y), self.pacman.getPos()) < 8):
            target = (1, 31)
        else:
            target = self.pacman.getPos()
        Ghost.update(self, target)