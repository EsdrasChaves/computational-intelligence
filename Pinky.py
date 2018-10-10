from Ghost import *

### Pinky behavior -- Tries to go to 4 Tiles ahead Pacman's position ###

class Pinky(Ghost):
    def __init__(self, mapa):
        Ghost.__init__(self, mapa, "pink", 26, 1)

    def update(self, pacman_pos, pacman_vel):
        target = tuple(map(sum, zip(pacman_pos, tuple(i * 4 for i in pacman_vel))))
        Ghost.update(self, target)