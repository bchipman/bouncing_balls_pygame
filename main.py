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
        while True:
            self.check_for_pygame_quit_event()
            self.window.surface.fill(BLACK)
            for ball in self.balls:
                ball.move()
                center_in_pixels = ball.center_absolute
                radius_in_pixels_tuple = ball.radius_absolute
                radius_in_pixels = radius_in_pixels_tuple[0]
                print('center_in_pixels', center_in_pixels)
                print('radius_in_pixels', radius_in_pixels)
                pygame.draw.circle(self.window.surface, ball.color, center_in_pixels, radius_in_pixels)
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
        self.total_number_balls = 3  # integer
        self.center_xy_range = (0.010, 0.99)  # proportion of window
        self.radius_range = (0.025, 0.075)  # proportion of window
        self.velocity_range = (0.005, 0.010)  # proportion of window
        self.window_size = (600, 600)  # pixels
if __name__ == '__main__':
    Main()
