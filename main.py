from ball_module import BallCreator
from colors import *
from collections import namedtuple
import pygame
import sys
import time
class Main:
    def __init__(self):
        self.options = Options()
        self.window = Window(self.options.window_size)
        self.balls = BallCreator(self.options).balls
        self.START_GAME_LOOP()
    def START_GAME_LOOP(self):
        while True:
            self.check_for_pygame_quit_event()
            self.window.surface.fill(BLACK)
            for ball in self.balls:
                ball.move(self.window)
                center_coordinate = Coordinate(ball.center)
                radius_coordinate = Coordinate((ball.radius, ball.radius))
                center_pixels = center_coordinate.absolute(self.window.size)
                radius_pixels = radius_coordinate.absolute(self.window.size)[0]
                pygame.draw.circle(self.window.surface, ball.color, center_pixels, radius_pixels)
                pygame.draw.circle(self.window.surface, ball.color, center_pixels, radius_pixels)
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
        pygame.display.set_caption('Version 0')
class Options:
    def __init__(self):
        self.total_number_balls = 3                 # integer
        self.center_xy_range = (0.010, 0.99)     # proportion of window
        self.radius_range = (0.025, 0.075)    # proportion of window
        self.velocity_range = (0.005, 0.010)    # proportion of window
        self.window_size = (600, 600)        # pixels
class Coordinate:
    def __init__(self, xy, total_size=None):
        x, y = xy
        if type(x) == type(y) == int:       # Given in pixels (absolute)
            W, H = total_size
            self._relative_x = x / W
            self._relative_y = y / H
        elif type(x) == type(y) == float:   # Given in proportions (relative)
            self._relative_x = x
            self._relative_y = y
    def relative(self):
        return (self._relative_x, self._relative_y)
    def absolute(self, absolute_size):
        W, H = absolute_size
        return (int(self._relative_x * W), int(self._relative_y * H))
        return (int(self._relative_x * W), int(self._relative_y * H))
if __name__ == '__main__':
    Main()
