#!python3
import generic_functions as gfs  # first because of syspath change
import ball
import os
import sys
import pygame
from colors import *
from pygame.locals import *
#-------------------------------------------------------------------------------
options = gfs.mk_namedtuple('Options', dict(
    total_number_balls  = 10,                   # integer
    center_xy_range     = (0.010,   0.99 ),     # proportion of window
    radius_range        = (0.025,   0.075),     # proportion of window
    velocity_range      = (0.005,   0.010),     # proportion of window
    window_size         = (  300,   300  ),     # pixels
    window_pos_desktop  = ( 2200,   150  ),     # pixels
    window_pos_laptop   = ( 1050,   150  ),     # pixels
    ))    
#-------------------------------------------------------------------------------
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

        def _setup_screen():
            display = pygame.display
            screen  = display.set_mode(options.window_size)
            display.set_caption('Bouncing Balls!')
            return screen

        def _setup_font():
            return pygame.font.SysFont(None, 24)

        _setup_window()
        _setup_mouse_keyboard()
        self.flash         = False
        self.pause         = False
        self.adv_one_frame = False
        self.frame_number  = 0
        self.screen        = _setup_screen()
        self.font          = _setup_font()
        self.balls         = ball.BallCreator(options).balls
    #-------------------------------------------------------------------------------
    def handle_events(self):
        def _check_for_quit_event():
            for event in self.curr_events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        def _check_for_key_press_events():
            for event in self.curr_events:
                if event.type == KEYDOWN:
                    if event.key == K_f:    
                        self.flash = True
                    if event.key == K_RIGHT:
                        self.adv_one_frame = True
                elif event.type == KEYUP:
                    if event.key == K_f:    
                        self.flash = False
                    if event.key == K_p:
                        if self.pause: 
                            self.pause = False
                        elif not self.pause: 
                            self.pause = True
        
        self.curr_events = pygame.event.get()
        self.mouse_position = pygame.mouse.get_pos()
        _check_for_quit_event()
        _check_for_key_press_events()
    #-------------------------------------------------------------------------------
    def draw_screen(self):
        def _draw_screen():
            if self.flash:
                self.screen.fill(RED)
            elif not self.flash:
                self.screen.fill(BLACK)
        
        def _draw_balls():
            for ball in self.balls:
                pygame.draw.circle(self.screen, ball.color, ball.position, ball.radius)
                self.screen.blit(ball.text_rendered, ball.text_position)
            pygame.draw.circle(self.screen, RED, self.mouse_position, 3)

        def _draw_mouse():
            pygame.draw.circle(self.screen, RED, self.mouse_position, 3)

        def _draw_frame_number():
            txt_rendered = self.font.render(str(self.frame_number), True, WHITE)
            self.screen.blit(txt_rendered, (0,0))

        def _update_screen():
            pygame.display.update()
            pygame.time.delay(50)
        
        _draw_screen()
        _draw_balls()
        _draw_mouse()
        _draw_frame_number()
        _update_screen()
    #-------------------------------------------------------------------------------
    def move_balls(self):
        self.balls = ball.BallHandler(self.balls, self.font)()
        self.frame_number += 1
    #-------------------------------------------------------------------------------
    def __call__(self):
        while True:
            self.handle_events()
            if self.pause and self.adv_one_frame:
                self.move_balls()
                self.draw_screen()
                self.pause = True
                self.adv_one_frame = False
            elif self.pause and not self.adv_one_frame:
                self.draw_screen()
            elif not self.pause:
                self.move_balls()
                self.draw_screen()
    #-------------------------------------------------------------------------------
if __name__ == '__main__':
    Main()()
