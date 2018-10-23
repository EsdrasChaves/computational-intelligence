from Ghost import *

### Pinky behavior -- Tries to go to 4 Tiles ahead Pacman's position ###

class Pinky(Ghost):
    def __init__(self, mapa, pacman):
        Ghost.__init__(self, mapa, "pink", 11, 11, pacman,1 + 3*TimeBetweenGhosts)

    def update(self):
        target = tuple(map(sum, zip(self.pacman.getPos(), tuple(i * 4 for i in self.pacman.getVel()))))
        Ghost.update(self, target)