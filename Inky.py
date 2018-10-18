from Ghost import *

### Inky behavior -- Trace a line between Blinky and 4 tiles ahead pacman, double the line length... ###

class Inky(Ghost):
    def __init__(self, mapa, pacman):
        Ghost.__init__(self, mapa, "blue", 26, 1, pacman)

    def update(self, blinky_pos):
        target_aux = tuple(map(sum, zip(self.pacman.getPos(), tuple(i * 4 for i in self.pacman.getVel()))))
        target = (2 * target_aux[0] - blinky_pos[0], 2 * target_aux[1] - blinky_pos[1])
        Ghost.update(self, target)