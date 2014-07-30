#!python3
import generic_functions as gfs  # first because of syspath change
import ball
import os
import sys
import pygame
from colors import *
from pygame.locals import *
import copy
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
            pygame.display.set_mode(options.window_size)
            pygame.display.set_caption('Bouncing Balls!')
            return pygame.display.get_surface()

        def _setup_font():
            return pygame.font.SysFont(None, 24)

        _setup_window()
        _setup_mouse_keyboard()
        self.flash          = False
        self.pause          = False
        self.adv_one_frame  = False
        self.frame_number   = 0
        self.surface        = _setup_screen()
        self.font           = _setup_font()
        self.balls          = ball.BallCreator(options).balls
        self.frame_history  = [list(self.balls)]
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
                    if event.key == K_f:        self.flash = True
                    if event.key == K_RIGHT:    self.adv_one_frame = True
                
                elif event.type == KEYUP:
                    if event.key == K_f:        self.flash = False
                    if event.key == K_p:
                        if       self.pause:    self.pause = False
                        elif not self.pause:    self.pause = True
                    if event.key == K_b:
                        if self.frame_number >= 10:
                            self.frame_number = 10
                            self.balls = copy.deepcopy(self.frame_history[self.frame_number])
        
        self.curr_events = pygame.event.get()
        self.mouse_position = pygame.mouse.get_pos()
        _check_for_quit_event()
        _check_for_key_press_events()
    #-------------------------------------------------------------------------------
    def move_balls(self):
        self.balls = ball.BallHandler(self.balls, self.font)()
        self.frame_number += 1
        self.frame_history.append(copy.deepcopy(self.balls))
    #-------------------------------------------------------------------------------
    def draw_screen(self):
        def _draw_screen():
            if self.flash:
                self.surface.fill(RED)
            elif not self.flash:
                self.surface.fill(BLACK)
        
        def _draw_balls():
            for ball in self.balls:
                pygame.draw.circle(self.surface, ball.color, ball.position, ball.radius)
                text = str(ball.number)
                text_rendered = self.font.render(text, True, BLACK)
                self.surface.blit(text_rendered, ball.text_position)

        def _draw_mouse():
            pygame.draw.circle(self.surface, RED, self.mouse_position, 3)

        def _draw_frame_number():
            txt_rendered = self.font.render(str(self.frame_number), True, WHITE)
            self.surface.blit(txt_rendered, (0,0))

        def _update_screen():
            pygame.display.update()
            pygame.time.delay(50)
        
        _draw_screen()
        _draw_balls()
        _draw_mouse()
        _draw_frame_number()
        _update_screen()
    #-------------------------------------------------------------------------------
    def __call__(self):
        while True:
            print(self.frame_number)
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
