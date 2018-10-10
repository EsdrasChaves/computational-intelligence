from Ghost import *

class Blinky(Ghost):
    def __init__(self, mapa):
        Ghost.__init__(self, mapa, "red", 26, 29)

    def update(self, pacman_pos):
        Ghost.update(self, pacman_pos)