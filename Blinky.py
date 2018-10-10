from Ghost import *

### Blinky behavior -- Tries to go to Pacman's position ###

class Blinky(Ghost):
    def __init__(self, mapa):
        Ghost.__init__(self, mapa, "red", 26, 29)

    def update(self, pacman_pos):
        Ghost.update(self, pacman_pos)