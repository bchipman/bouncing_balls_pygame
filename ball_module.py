import calculate
import colors
import random
class Ball:
    def __init__(self, number, center, radius, velocity, color):
        self.identity = number
        self.center = center
        self.radius = radius
        self.velocity = velocity
        self.color = color
        self.edges = calculate.edge_values(self.center, self.radius)
    def move(self, window):
        x,   y = self.center
        dx, dy = self.velocity
        self.center = (x + dx, y + dy)
        self.edges = calculate.edge_values(self.center, self.radius)
        self._change_direction_if_necessary(window)
    def _change_direction_if_necessary(self, window):
        if calculate.wall_collision(self, window):
            wall_that_was_hit = calculate.wall_hit(self, window)
            new_velocity = calculate.velocity_after_wall_collision_v0(self, wall_that_was_hit)
            self.velocity = new_velocity
class BallCreator:
    def __init__(self, options):
        self.number_balls = options.total_number_balls
        self.center_xy_range = options.center_xy_range
        self.radius_range = options.radius_range
        self.velocity_range = options.velocity_range
        self.balls = self._setup_balls()
    def _setup_balls(self):
        balls = []
        for n in range(0, self.number_balls):
            ball = self._create_random_ball(n)
            balls.append(ball)
        return balls
    def _create_random_ball(self, N):
        xy, XY = self.center_xy_range
        r, R = self.radius_range
        v, V = self.velocity_range
        X = BallCreator.RND(self.center_xy_range)
        Y = BallCreator.RND(self.center_xy_range)
        R = BallCreator.RND(self.radius_range)
        V = BallCreator.RND(self.velocity_range)
        V = BallCreator.RND([-V, V])
        C = BallCreator.RND(colors.colors)
        return Ball(number=N, center=(X, Y), radius=R, velocity=(V, V), color=C)
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
if __name__ == '__main__':
    pass
