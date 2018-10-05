import pygame


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FPS = 10


class Pacman(object):
    RADIUS = 20
    WIDTH_IN_TILES = WINDOW_WIDTH / RADIUS

    def __init__(self):
        self.pos_x = 1
        self.pos_y = 1

        self.vel_x = 1
        self.vel_y = 0

    def update(self, events):
        self.vel_x, self.vel_y = self.handle_mov(events)
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.check_borders()

    def draw(self, win):
        pygame.draw.circle(
            win,
            pygame.color.Color("yellow"),
            (
                self.pos_x * self.RADIUS,
                self.pos_y * self.RADIUS,
            ), self.RADIUS
        )

    def handle_mov(self, events):
        movement = (self.vel_x, self.vel_y)
        vel_list = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    movement = vel_list['up']
                elif event.key == pygame.K_DOWN:
                    movement = vel_list['down']
                elif event.key == pygame.K_LEFT:
                    movement = vel_list['left']
                elif event.key == pygame.K_RIGHT:
                    movement = vel_list['right']
        return movement

    def check_borders(self):
        if self.pos_x > self.WIDTH_IN_TILES - 1 or self.pos_x <= 0:
            end_game()
        elif self.pos_y > self.WIDTH_IN_TILES - 1 or self.pos_y <= 0:
            end_game()



def run():
    pygame.init()
    win = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT),
        pygame.HWSURFACE
    )
    pygame.display.set_caption("PacMan-Game")
    game_loop(win)


def game_loop(win):
    pacman = Pacman()
    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        handle_quit(events)

        win.fill((0, 0, 0))

        pacman.update(events)
        pacman.draw(win)

        pygame.display.update()
        clock.tick(FPS)


def handle_quit(events):
    for event in events:
        if event.type == pygame.QUIT:
            end_game()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            end_game()


def end_game():
    pygame.quit()
    exit(0)


run()
