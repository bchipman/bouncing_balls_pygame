import calculate
import colors
import itertools
import globals
from coordinate import Coordinate


class Ball:
    def __init__(self, number, color, center, radius, velocity):
        w_size                  = globals.window_size()
        self.number             = number
        self.color              = color
        self.start_color        = color

        self.position     = Coordinate(center)
        self.radius       = Coordinate((radius,radius))
        self.velocity     = Coordinate(velocity)
        self.edges        = calculate.edge_values(self.position.rel, self.radius.rel)
        self.walls_hit    = calculate.walls_hit(self.edges)
        self.text_position= calculate.ball_text_position(str(self.number), globals.font(), self.position.abs, w_size)

    def __repr__(self):
        return 'Ball N:{}, XY:{}, R:{}'.format(self.number, self.position, self.radius)


class BallCreator:
    def __init__(self):
        self.number_balls       = globals.options.total_number_balls
        self.center_xy_range    = globals.options.center_xy_range
        self.radius_range       = globals.options.radius_range
        self.velocity_range     = globals.options.velocity_range
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
        C = globals.rnd(colors.ball_colors)
        X = globals.rnd(self.center_xy_range)
        Y = globals.rnd(self.center_xy_range)
        R = globals.rnd(self.radius_range)
        V = globals.rnd(self.velocity_range)
        V = globals.rnd([-V, V])
        return Ball(number=N, color=C, center=(X, Y), radius=R, velocity=(V, V))

    def _new_ball_not_in_wall(self, ball):
        edges = calculate.edge_values(ball.position.rel, ball.radius.rel)
        walls_hit = calculate.walls_hit(edges)
        if walls_hit == '': return True
        else:               return False

    def _new_ball_not_in_other_ball(self, new_ball, balls_so_far):
        for old_ball in balls_so_far:
            if calculate.ball_collision(old_ball.position.rel, old_ball.radius.rel, new_ball.position.rel, new_ball.radius.rel):
                return False
        return True


class BallHandler:
    def __init__(self, balls):
        self.balls = balls

    def __call__(self):
        self._move_balls()
        self._check_for_overlaps()
        self._change_colors_when_hit()
        self._get_ball_text_position()
        # self._get_new_velocities()
        self._print_collisions()
        return self.balls
        
    def _move_balls(self):
        for ball in self.balls:
            ball.position   = Coordinate(calculate.new_position(ball.position.rel, ball.velocity.rel))
            ball.edges      = calculate.edge_values(ball.position.rel, ball.radius.rel)
            ball.walls_hit  = calculate.walls_hit(ball.edges)
            ball.velocity   = Coordinate(calculate.velocity_after_wall_collision(ball.velocity.rel, ball.walls_hit))

    def _check_for_overlaps(self):
        combos = itertools.combinations(self.balls, 2)
        self.ball_collisions = [(a.number,b.number) for (a,b) in combos if calculate.ball_collision(a.position.rel, a.radius.rel, b.position.rel, b.radius.rel)]
        self.balls_hit_other_ball = set([item for inner_iterable in self.ball_collisions for item in inner_iterable])
        self.balls_hit_wall = set([ball.number for ball in self.balls if ball.walls_hit != ''])
    
    def _change_colors_when_hit(self):
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
            ball.text_position = Coordinate(calculate.ball_text_position(text, globals.font(), ball.position.abs, globals.window_size()), globals.window_size())

    def _get_new_velocities(self):
        for i, j in self.ball_collisions:
            new_vels = calculate.velocity_after_ball_collision(self.balls[i], self.balls[j])
            self.balls[i].velocity, self.balls[j].velocity = new_vels 

    def _print_collisions(self):
        print('{:<5}'.format(globals.frame_number)+'  '.join([str(i)[1:-1].replace(', ', '~') for i in self.ball_collisions]))


if __name__ == '__main__':
    import main
    main.Main()()
