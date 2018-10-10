from Ghost import *

### Inky behavior -- Trace a line between Blinky and 4 tiles ahead pacman, double the line length... ###

class Inky(Ghost):
    def __init__(self, mapa):
        Ghost.__init__(self, mapa, "blue", 1, 1)

    def update(self, pacman_pos, pacman_vel, blinky_pos):
        target_aux = tuple(map(sum, zip(pacman_pos, tuple(i * 4 for i in pacman_vel))))
        target = (2 * target_aux[0] - blinky_pos[0], 2 * target_aux[1] - blinky_pos[1])
        Ghost.update(self, target)