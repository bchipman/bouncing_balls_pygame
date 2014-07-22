import calculate
import colors
import random


class Ball:
    def __init__(self, number, color, center, radius, velocity, window_size):
        self.number             = number
        self.color              = color
        self.start_color        = color
        self.center_absolute    = Coordinate(center).absolute(window_size)
        self.radius_absolute    = Coordinate((radius,radius)).absolute(window_size)[0]
        self.velocity_absolute  = Coordinate(velocity).absolute(window_size)
        self.window_size        = window_size
        self.ball_edges         = calculate.edge_values(self.center_absolute, self.radius_absolute)
        self.walls_hit          = calculate.walls_hit(self.ball_edges, self.window_size)        
        self.hit_counter        = 0

    def move(self):
        self.center_absolute = calculate.new_position(self.center_absolute, self.velocity_absolute)
        self.ball_edges = calculate.edge_values(self.center_absolute, self.radius_absolute)
        self.walls_hit = calculate.walls_hit(self.ball_edges, self.window_size)
        self.velocity_absolute = calculate.velocity_after_wall_collision(self.velocity_absolute, self.walls_hit)
        self._change_color_if_collision()
        return (self.center_absolute, self.radius_absolute)

    def _change_color_if_collision(self):
        if self.walls_hit == '':  # if no walls hit this frame..
            self.hit_counter = self.hit_counter - 1 if self.hit_counter > 0 else 0  # ..decrement if necessary
            if self.hit_counter == 0:  # if counter is at 0..
                self.color = self.start_color  # ..set ball color to starting color
        else: # if walls were hit this frame..
            self.color = colors.YELLOW  # ..set ball color to yellow
            self.hit_counter = 5  # ..and reset counter


class BallCreator:
    def __init__(self, options):
        self.number_balls       = options.total_number_balls
        self.center_xy_range    = options.center_xy_range
        self.radius_range       = options.radius_range
        self.velocity_range     = options.velocity_range
        self.window_size        = options.window_size
        self.balls              = self._setup_balls()

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
    def RND(range_or_choices):
        if type(range_or_choices) is tuple:
            a, b = range_or_choices
            if type(a) == type(b) == int:
                return random.randint(a, b)
            elif type(a) == type(b) == float:
                return random.uniform(a, b)
        elif type(range_or_choices) is list:
            return random.choice(range_or_choices)


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


if __name__ == '__main__':
    import main
    main.Main()