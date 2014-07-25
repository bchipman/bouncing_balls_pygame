#!python3
import generic_functions as gfs
gfs.change_sys_path()
import ball_module
from colors import *
import os
import sys
import pygame


options = gfs.mk_namedtuple('Options', dict(
    total_number_balls  = 10,                   # integer
    center_xy_range     = (0.010,   0.99 ),     # proportion of window
    radius_range        = (0.025,   0.075),     # proportion of window
    velocity_range      = (0.005,   0.010),     # proportion of window
    window_size         = (  300,   300  ),     # pixels
    window_pos_desktop  = ( 2200,   150  ),     # pixels
    window_pos_laptop   = ( 1050,   150  ),     # pixels
    ))    


class Main:
    def __init__(self):
        def _setup_window():
            if os.environ['COMPUTERNAME'] == 'BRIAN-DESKTOP':
                os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(options.window_pos_desktop[0], options.window_pos_desktop[1])  # positions window

            elif os.environ['COMPUTERNAME'] == 'BRIAN-LAPTOP':
                os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(options.window_pos_laptop[0], options.window_pos_laptop[1])  # positions window
            pygame.init()

        def _setup_font():
            return pygame.font.SysFont(None, 14)

        def _setup_screen():
            display = pygame.display
            screen  = display.set_mode(options.window_size)
            display.set_caption('Bouncing Balls!')
            return screen
        
        _setup_window()
        self.screen  = _setup_screen()
        self.font    = _setup_font()
        self.balls   = ball_module.BallCreator(options).balls
        self.START_GAME_LOOP()

    def START_GAME_LOOP(self):

        def _check_for_pygame_quit_event():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        def _redraw_screen():
            self.screen.fill(BLACK)
            self.balls = ball_module.ActionHandler(self.balls, self.font)()
            for ball in self.balls:
                pygame.draw.circle(self.screen, ball.color, ball.position, ball.radius)
                self.screen.blit(ball.text_rendered, ball.text_position)

            pygame.display.update()
            pygame.time.delay(50)

        while True:
            _check_for_pygame_quit_event()
            _redraw_screen()


if __name__ == '__main__':
    Main()
