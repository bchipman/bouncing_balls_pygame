import ball_module
from colors import *
import pygame
import sys


class Main:
    def __init__(self):
        self.options = Options()
        self.window = Window(self.options.window_size)
        self.balls = ball_module.BallCreator(self.options).balls
        self.START_GAME_LOOP()

    def START_GAME_LOOP(self):
        pygame.init()
        while True:
            self.check_for_pygame_quit_event()
            self.window.surface.fill(BLACK)
            for ball in self.balls:
                center_pos_px, radius_px =  ball.move()
                print('center_pos_px', center_pos_px)
                print('radius_px', radius_px)
                pygame.draw.circle(self.window.surface, ball.color, center_pos_px, radius_px[0])
                basic_font = pygame.font.SysFont(None, 24)
                text = basic_font.render(str(ball.number), True, BLACK)
                self.window.surface.blit(text, center_pos_px)
                
            pygame.display.update()
            pygame.time.delay(20)

    def check_for_pygame_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


class Window:
    def __init__(self, size):
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption('Version 1')


class Options:
    def __init__(self):
        self.total_number_balls = 10  # integer
        self.center_xy_range = (0.010, 0.99)  # proportion of window
        self.radius_range = (0.025, 0.075)  # proportion of window
        self.velocity_range = (0.005, 0.010)  # proportion of window
        self.window_size = (600, 600)  # pixels


if __name__ == '__main__':
    Main()
