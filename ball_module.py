import calculate
import colors
import itertools
import generic_functions


class Ball:
    def __init__(self, number, color, center, radius, velocity, window_size):
        self.number             = number
        self.color              = color
        self.start_color        = color
        self.position           = Coordinate(center).absolute(window_size)
        self.radius             = Coordinate((radius,radius)).absolute(window_size)[0]
        self.velocity           = Coordinate(velocity).absolute(window_size)
        self.window_size        = window_size
        self.edges              = calculate.edge_values(self.position, self.radius)
        self.walls_hit          = calculate.walls_hit(self.edges, self.window_size)


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
                    if self._new_ball_not_in_other_ball(ball, balls):
                        break
            balls.append(ball)
        return balls

    def _create_random_ball(self, N):
        xy, XY = self.center_xy_range
        r, R = self.radius_range
        v, V = self.velocity_range
        C = generic_functions.rnd(colors.ball_colors)
        X = generic_functions.rnd(self.center_xy_range)
        Y = generic_functions.rnd(self.center_xy_range)
        R = generic_functions.rnd(self.radius_range)
        V = generic_functions.rnd(self.velocity_range)
        V = generic_functions.rnd([-V, V])
        return Ball(number=N, color=C, center=(X, Y), radius=R, velocity=(V, V), window_size=self.window_size)

    def _new_ball_not_in_wall(self, ball):
        edges = calculate.edge_values(ball.position, ball.radius)
        walls_hit = calculate.walls_hit(edges, ball.window_size)
        if walls_hit == '': return True
        else:               return False
    
    def _new_ball_not_in_other_ball(self, new_ball, balls_so_far):
        for old_ball in balls_so_far:
            if calculate.ball_collision(old_ball.position, old_ball.radius, new_ball.position, new_ball.radius):
                return False
        return True


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


class ActionHandler:
    def __init__(self, balls, font):
        self.balls = balls
        self.font = font

    def __call__(self):
        self._move_balls()
        self._check_for_overlaps()
        self._get_ball_text_position()
        self._print_collisions()
        return self.balls
        
    def _move_balls(self):
        for ball in self.balls:
            ball.position   = calculate.new_position(ball.position, ball.velocity)
            ball.edges      = calculate.edge_values(ball.position, ball.radius)
            ball.walls_hit  = calculate.walls_hit(ball.edges, ball.window_size)
            ball.velocity   = calculate.velocity_after_wall_collision(ball.velocity, ball.walls_hit)

    def _check_for_overlaps(self):
        combos = itertools.combinations(self.balls, 2)
        self.ball_collisions = [(a.number,b.number) for (a,b) in combos if calculate.ball_collision(a.position, a.radius, b.position, b.radius)]
        self.balls_hit_other_ball = set([item for inner_iterable in self.ball_collisions for item in inner_iterable])
        self.balls_hit_wall = set([ball.number for ball in self.balls if ball.walls_hit != ''])
        for ball in self.balls:
            ball.color = ball.start_color
            if ball.number in self.balls_hit_wall:
                ball.color = colors.YELLOW
                if ball.number in self.balls_hit_other_ball:
                    ball.color = colors.RED
            elif ball.number in self.balls_hit_other_ball:
                ball.color = colors.ORANGE

    def _get_ball_text_position(self):
        for ball in self.balls:
            text = str(ball.number)
            ball.text_position = calculate.ball_text_position(text, self.font, ball.position)
            ball.text_rendered = self.font.render(text, True, colors.BLACK)

    def _print_collisions(self):
        print('    '.join([str(i)[1:-1].replace(', ', '~') for i in self.ball_collisions]))


if __name__ == '__main__':
    import main
    main.Main()
