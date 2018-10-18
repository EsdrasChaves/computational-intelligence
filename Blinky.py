from Ghost import *

### Blinky behavior -- Tries to go to Pacman's position ###

class Blinky(Ghost):
    def __init__(self, mapa, pacman):
        Ghost.__init__(self, mapa, "red", 12, 11, pacman)

    def update(self):
        Ghost.update(self, self.pacman.getPos())