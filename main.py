import generic_functions as gfs
gfs.change_sys_path()
import ball_module
from colors import *
import sys
import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.options = options
        self.screen  = self.setup_screen()
        self.font    = self.setup_font()
        self.balls   = ball_module.BallCreator(self.options).balls
        self.START_GAME_LOOP()

    def setup_font(self):
        return pygame.font.SysFont(None, 24)

    def setup_screen(self):
        display = pygame.display
        screen  = display.set_mode(self.options.window_size)
        display.set_caption('Bouncing Balls!')
        return screen

    def START_GAME_LOOP(self):
        while True:
            self.check_for_pygame_quit_event()
            self.redraw_screen()

    def check_for_pygame_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def redraw_screen(self):
        self.screen.fill(BLACK)
        for ball in self.balls:
            center_pos_px, radius_px = ball.move()
            pygame.draw.circle(self.screen, ball.color, center_pos_px, radius_px)
            text = self.font.render(str(ball.number), True, BLACK)
            self.screen.blit(text, center_pos_px)
        pygame.display.update()
        pygame.time.delay(50)


options = gfs.mk_namedtuple('Options', dict(
    total_number_balls  = 5,                # integer
    center_xy_range     = (0.010,   0.99),  # proportion of window
    radius_range        = (0.025,   0.075), # proportion of window
    velocity_range      = (0.005,   0.010), # proportion of window
    window_size         = (600,     600)))  # pixels


if __name__ == '__main__':
    Main()
