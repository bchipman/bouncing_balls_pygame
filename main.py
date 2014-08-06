import copy
import os
import sys

import globals  # must be before pygame else python warning
import ball
import pygame

from colors         import *
from pygame.locals  import *
#-------------------------------------------------------------------------------
class Main:
    def __init__(self):
        def _setup_window():
            start_pos = globals.Options.window_pos_desktop
            if os.environ['COMPUTERNAME'] == 'BRIAN-LAPTOP':
                start_pos = globals.Options.window_pos_laptop
            os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(start_pos[0], start_pos[1])  # positions window
            pygame.init()
        
        def _setup_mouse_keyboard():
            pygame.mouse.set_visible(False)
            pygame.key.set_repeat(500, 100)

        def _setup_screen():
            pygame.display.set_mode(globals.Options.initial_window_size, RESIZABLE)
            pygame.display.set_caption('Bouncing Balls!')
            return pygame.display.get_surface()

        def _setup_font():
            return globals.font()

        _setup_window()
        _setup_mouse_keyboard()
        self.flash              = False
        self.pause              = False
        self.adv_one_frame      = False
        self.rev_one_frame      = False
        globals.frame_number    = 0
        self.surface            = _setup_screen()
        self.font               = _setup_font()
        self.balls              = ball.BallCreator().balls
        self.frame_history      = {0:copy.deepcopy(self.balls)}
        self.frame_dir          = 1
    #-------------------------------------------------------------------------------
    def handle_events(self):
        def _handle_key_press_events():
            for event in pygame.event.get([KEYDOWN, KEYUP]):
            
                if event.type == KEYDOWN:
                    # multiple KEYDOWN events set to occur when key is held down
                    if event.key == K_f:        self.flash = True
                    if event.key == K_RIGHT:    self.adv_one_frame = True
                    if event.key == K_LEFT:     self.rev_one_frame = True
                
                elif event.type == KEYUP:
                    if event.key == K_q:
                        pygame.event.post(pygame.event.Event(QUIT))

                    if event.key == K_f:        self.flash = False
                    if event.key == K_SPACE:    self.pause = not self.pause
                    if event.key == K_r:
                        globals.frame_number = 0
                        self.balls = copy.deepcopy(self.frame_history[globals.frame_number])
        
        def _handle_pause():
            if self.pause:
                self.frame_dir = 0
                if self.adv_one_frame:
                    self.adv_one_frame = False
                    self.frame_dir = 1
                elif self.rev_one_frame:
                    self.rev_one_frame = False
                    self.frame_dir = -1
            elif not self.pause:
                self.frame_dir = 1

        def _handle_resize_event():
            for event in pygame.event.get(VIDEORESIZE):
                new_size = event.size
                new_size_forced_square = (min(new_size), min(new_size))
                pygame.display.set_mode(new_size_forced_square, RESIZABLE)

        def _handle_quit_event():
            for event in pygame.event.get(QUIT):
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        
        self.mouse_position = pygame.mouse.get_pos()
        _handle_key_press_events()
        _handle_pause()
        _handle_resize_event()
        _handle_quit_event()
        pygame.event.clear()
    #-------------------------------------------------------------------------------
    def handle_frames(self):

        def _change_frame_number():
            globals.frame_number += self.frame_dir
            if globals.frame_number < 0:   globals.frame_number = 0

        def _retrieve_or_generate_ball_data():
            if globals.frame_number in self.frame_history:  # frame already occurred 
                self.balls = copy.deepcopy(self.frame_history[globals.frame_number]) 
            elif globals.frame_number not in self.frame_history:  # frame hasn't happened yet 
                self.balls = ball.BallHandler(self.balls)()
        
        def _save_new_ball_data():
            if globals.frame_number not in self.frame_history:  # frame hasn't happened yet
                self.frame_history[globals.frame_number] = copy.deepcopy(self.balls)  # add data to frame history
        
        _change_frame_number()
        _retrieve_or_generate_ball_data()
        _save_new_ball_data()
    #-------------------------------------------------------------------------------
    def draw_screen(self):
        def _draw_screen():
            if self.flash:
                self.surface.fill(RED)
            elif not self.flash:
                self.surface.fill(BLACK)
        
        def _draw_balls():
            for ball in self.balls:
                pygame.draw.circle(self.surface, ball.color, ball.position.abs, ball.radius.abs[0])
                text_rendered = self.font.render(str(ball.number), True, BLACK)
                self.surface.blit(text_rendered, ball.text_position.abs)

        def _draw_mouse():
            pygame.draw.circle(self.surface, RED, self.mouse_position, 3)

        def _draw_frame_number():
            txt_rendered = self.font.render(str(globals.frame_number), True, WHITE)
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
            self.handle_events()
            self.handle_frames()
            self.draw_screen()
    #-------------------------------------------------------------------------------
if __name__ == '__main__':
    Main()()
