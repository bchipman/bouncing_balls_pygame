import generic_functions as gfs
gfs.change_sys_path()
import ball_module
from colors import *
import os
import sys
import pygame


class Main:
    def __init__(self):
        def _setup_pygame():
            if os.environ['COMPUTERNAME'] == 'BRIAN-LAPTOP':
                os.environ['SDL_VIDEO_WINDOW_POS'] = "1050, 150"  # positions window
            pygame.init()

        def _setup_font():
            return pygame.font.SysFont(None, 14)

        def _setup_screen():
            display = pygame.display
            screen  = display.set_mode(self.options.window_size)
            display.set_caption('Bouncing Balls!')
            return screen
        
        _setup_pygame()
        self.options = options
        self.font    = _setup_font()
        self.screen  = _setup_screen()
        self.balls   = ball_module.BallCreator(self.options).balls
        self.START_GAME_LOOP()

    def START_GAME_LOOP(self):

        def _check_for_pygame_quit_event():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        def _redraw_screen():
            self.screen.fill(BLACK)
            self.balls = ball_module.move_balls(self.balls)
            for ball in self.balls:
                pygame.draw.circle(self.screen, ball.color, ball.position, ball.radius)
                text = self.font.render(str(ball.number), True, BLACK)
                self.screen.blit(text, ball.position)
            pygame.display.update()
            pygame.time.delay(50)

        while True:
            _check_for_pygame_quit_event()
            _redraw_screen()


options = gfs.mk_namedtuple('Options', dict(
    total_number_balls  = 10,                   # integer
    center_xy_range     = (0.010,   0.99 ),     # proportion of window
    radius_range        = (0.025,   0.075),     # proportion of window
    velocity_range      = (0.005,   0.010),     # proportion of window
    window_size         = (300,     300  )))    # pixels


if __name__ == '__main__':
    Main()
