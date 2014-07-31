#!python3
import globals  # first because of syspath change
import ball
import copy
import os
import sys
import pygame
from colors import *
from pygame.locals import *
#-------------------------------------------------------------------------------
class Main:
    def __init__(self):
        def _setup_window():
            start_pos = globals.options.window_pos_desktop
            if os.environ['COMPUTERNAME'] == 'BRIAN-LAPTOP':
                start_pos = globals.options.window_pos_laptop
            os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(start_pos[0], start_pos[1])  # positions window
            pygame.init()
        
        def _setup_mouse_keyboard():
            pygame.mouse.set_visible(False)
            pygame.key.set_repeat(500, 100)

        def _setup_screen():
            pygame.display.set_mode(globals.options.window_size)
            pygame.display.set_caption('Bouncing Balls!')
            return pygame.display.get_surface()

        def _setup_font():
            return globals.font()

        _setup_window()
        _setup_mouse_keyboard()
        self.flash          = False
        self.pause          = False
        self.adv_one_frame  = False
        self.rev_one_frame  = False
        self.frame_number   = 0
        self.max_frame      = 0
        self.surface        = _setup_screen()
        self.font           = _setup_font()
        self.balls          = ball.BallCreator().balls
        self.frame_history  = {0:copy.deepcopy(self.balls)}
        self.frame_dir      = 1
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
                    # multiple KEYDOWN events set to occur when key is held down
                    if event.key == K_f:        self.flash = True
                    if event.key == K_RIGHT:    self.adv_one_frame = True
                    if event.key == K_LEFT:     self.rev_one_frame = True
                
                elif event.type == KEYUP:
                    if event.key == K_f:        self.flash = False
                    if event.key == K_SPACE:    self.pause = not self.pause
                    if event.key == K_b:
                        if self.frame_number >= 10:
                            self.frame_number = 10
                            self.balls = copy.deepcopy(self.frame_history[self.frame_number])
        
        self.curr_events = pygame.event.get()
        self.mouse_position = pygame.mouse.get_pos()
        _check_for_quit_event()
        _check_for_key_press_events()
    #-------------------------------------------------------------------------------
    def handle_frames(self):
        def _move_balls():
            self.frame_number += self.frame_dir
            self.max_frame = max(self.max_frame, self.frame_number)
            if self.frame_number < 0:   self.frame_number = 0

            if self.frame_number in self.frame_history.keys():  # frame already occurred 
                self.balls = copy.deepcopy(self.frame_history[self.frame_number]) 

            elif self.frame_number not in self.frame_history.keys():  # frame hasn't happened yet 
                self.balls = ball.BallHandler(self.balls, self.font)()
            self.frame_history[self.frame_number] = copy.deepcopy(self.balls)  # add data to frame history

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
        
        _move_balls()        
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
                text_rendered = self.font.render(str(ball.number), True, BLACK)
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
            self.handle_events()
            self.handle_frames()
            self.draw_screen()
    #-------------------------------------------------------------------------------
if __name__ == '__main__':
    Main()()
