import calculate
import colors
import random


class Ball:
    def __init__(self, number, color, center, radius, velocity, window_size):
        self.number             = number
        self.color              = color
        self.start_color        = color
        self.position           = Coordinate(center).absolute(window_size)
        self.radius             = Coordinate((radius,radius)).absolute(window_size)[0]
        self.velocity           = Coordinate(velocity).absolute(window_size)
        self.window_size        = window_size
        self.ball_edges         = calculate.edge_values(self.position, self.radius)
        self.walls_hit          = calculate.walls_hit(self.ball_edges, self.window_size)        
        self.hit_counter        = 0


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
        ball_edges = calculate.edge_values(ball.position, ball.radius)
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


def move_all_balls(balls):
    for ball in balls:
        ball.position   = calculate.new_position(ball.position, ball.velocity)
        ball.ball_edges = calculate.edge_values(ball.position, ball.radius)
        ball.walls_hit  = calculate.walls_hit(ball.ball_edges, ball.window_size)
        ball.velocity   = calculate.velocity_after_wall_collision(ball.velocity, ball.walls_hit)
    return balls









if __name__ == '__main__':
    import main
    main.Main()
