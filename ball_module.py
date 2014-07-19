import calculate
import colors
import random


class Ball:
    def __init__(self, number, color, center, radius, velocity, window_size):
        self.window_size = window_size
        self.number = number
        self.color = color
        self.original_color = color
        radius_Coordinate = Coordinate((radius, radius))  # calculate absolute version only once, at beginning (assuming window cannot be resized)
        self.radius_absolute = radius_Coordinate.absolute(window_size)
        velocity_Coordinate = Coordinate(velocity)          # calculate absolute version only once, at beginning (assuming window cannot be resized)
        self.velocity_absolute = velocity_Coordinate.absolute(window_size)
        center_Coordinate = Coordinate(center)            # calculate absolute version only once, at beginning (assuming window cannot be resized)
        self.center_absolute = center_Coordinate.absolute(window_size)

    def move(self):
        x_abs, y_abs = self.center_absolute
        dx_abs, dy_abs = self.velocity_absolute
        new_x_abs = x_abs + dx_abs
        new_y_abs = y_abs + dy_abs
        new_xy_abs = new_x_abs, new_y_abs
        self.center_absolute = new_xy_abs
        self._change_velocity_direction_if_necessary(new_xy_abs)
        return (self.center_absolute, self.radius_absolute)

    def _change_velocity_direction_if_necessary(self, new_position_abs):
        ball_edges = calculate.edge_values(new_position_abs, self.radius_absolute)
        walls_hit = calculate.walls_hit(ball_edges, self.window_size)
        if walls_hit != '': self.color = colors.YELLOW
        else:               self.color = self.original_color
        new_velocity_abs = calculate.velocity_after_wall_collision(self.velocity_absolute, walls_hit)
        self.velocity_absolute = new_velocity_abs


class BallCreator:
    def __init__(self, options):
        self.number_balls = options.total_number_balls
        self.center_xy_range = options.center_xy_range
        self.radius_range = options.radius_range
        self.velocity_range = options.velocity_range
        self.window_size = options.window_size
        self.balls = self._setup_balls()

    def _setup_balls(self):
        balls = []
        for n in range(0, self.number_balls):
            while True:
                ball = self._create_random_ball(n)
                if self._new_ball_not_in_wall(ball):
                    break
            balls.append(ball)
        return balls

    def _create_random_ball(self, N):
        xy, XY = self.center_xy_range
        r, R = self.radius_range
        v, V = self.velocity_range
        C = BallCreator.RND(colors.colors)
        X = BallCreator.RND(self.center_xy_range)
        Y = BallCreator.RND(self.center_xy_range)
        R = BallCreator.RND(self.radius_range)
        V = BallCreator.RND(self.velocity_range)
        V = BallCreator.RND([-V, V])
        return Ball(number=N, color=C, center=(X, Y), radius=R, velocity=(V, V), window_size=self.window_size)

    def _new_ball_not_in_wall(self, ball):
        ball_edges = calculate.edge_values(ball.center_absolute, ball.radius_absolute)
        walls_hit = calculate.walls_hit(ball_edges, ball.window_size)
        if walls_hit == '': return True
        else:               return False

    @staticmethod
    def RND(range_or_options):
        if type(range_or_options) is tuple:
            a, b = range_or_options
            if type(a) == type(b) == int:
                return random.randint(a, b)
            elif type(a) == type(b) == float:
                return random.uniform(a, b)
        elif type(range_or_options) is list:
            return random.choice(range_or_options)


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
