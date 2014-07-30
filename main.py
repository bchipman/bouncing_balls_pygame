#!python3
import generic_functions as gfs
gfs.change_sys_path()
import ball_module
from colors import *
import os
import sys
import pygame
from pygame.locals import *


options = gfs.mk_namedtuple('Options', dict(
    total_number_balls  = 10,                   # integer
    center_xy_range     = (0.010,   0.99 ),     # proportion of window
    radius_range        = (0.025,   0.075),     # proportion of window
    velocity_range      = (0.005,   0.010),     # proportion of window
    window_size         = (  300,   300  ),     # pixels
    window_pos_desktop  = ( 2200,   150  ),     # pixels
    window_pos_laptop   = ( 1050,   150  ),     # pixels
    ))    


class G:
    pass


class Main:
    def __init__(self):
        def _setup_window():
            start_pos = options.window_pos_desktop
            if os.environ['COMPUTERNAME'] == 'BRIAN-LAPTOP':
                start_pos = options.window_pos_laptop
            os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(start_pos[0], start_pos[1])  # positions window
            pygame.init()
        
        def _setup_mouse_keyboard():
            pygame.mouse.set_visible(False)
            pygame.key.set_repeat(500, 100)

        def _setup_font():
            return pygame.font.SysFont(None, 24)

        def _setup_screen():
            display = pygame.display
            screen  = display.set_mode(options.window_size)
            display.set_caption('Bouncing Balls!')
            return screen

        _setup_window()
        _setup_mouse_keyboard()
        G.flash         = False
        G.pause         = False
        G.adv_one_frame = False
        G.screen        = _setup_screen()
        G.font          = _setup_font()
        G.balls         = ball_module.BallCreator(options).balls
    #-------------------------------------------------------------------------------
    def __call__(self):
        while True:
            self.handle_events()
            if G.pause:
                if G.adv_one_frame:
                    self.move_balls()
                    self.draw_screen()
                    G.pause = True
                    G.adv_one_frame = False
                else:
                    self.draw_screen()

            elif not G.pause:
                self.move_balls()
                self.draw_screen()
    #-------------------------------------------------------------------------------
    def handle_events(self):
        def _check_for_quit_event():
            for event in G.curr_events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        def _check_for_key_press_events():
            for event in G.curr_events:
                if event.type == KEYDOWN:
                    if event.key == K_f:    
                        G.flash = True
                    if event.key == K_RIGHT:
                        G.adv_one_frame = True
                elif event.type == KEYUP:
                    if event.key == K_f:    
                        G.flash = False
                    if event.key == K_p:
                        if G.pause: 
                            G.pause = False
                        elif not G.pause: 
                            G.pause = True
        
        G.curr_events = pygame.event.get()
        G.mouse_position = pygame.mouse.get_pos()
        _check_for_quit_event()
        _check_for_key_press_events()
    #-------------------------------------------------------------------------------
    def draw_screen(self):
        def _draw_screen():
            if G.flash:
                G.screen.fill(RED)
            elif not G.flash:
                G.screen.fill(BLACK)
        
        def _draw_balls():
            for ball in G.balls:
                pygame.draw.circle(G.screen, ball.color, ball.position, ball.radius)
                G.screen.blit(ball.text_rendered, ball.text_position)
            pygame.draw.circle(G.screen, RED, G.mouse_position, 3)

        def _draw_mouse():
            pygame.draw.circle(G.screen, RED, G.mouse_position, 3)

        def _update_screen():
            pygame.display.update()
            pygame.time.delay(50)
        
        _draw_screen()
        _draw_balls()
        _draw_mouse()
        _update_screen()
    #-------------------------------------------------------------------------------
    def move_balls(self):
        G.balls = ball_module.BallHandler(G.balls, G.font)()

if __name__ == '__main__':
    Main()()
