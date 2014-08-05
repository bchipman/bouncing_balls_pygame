import math
from coordinate import Coordinate

def edge_values(position, radius):
    x, y = position
    if type(radius) is tuple:   r, r = radius
    else:                       r    = radius
    U = y - r
    D = y + r
    L = x - r
    R = x + r
    return (U, D, L, R)

def walls_hit(ball_edges):
    Up, Dn, L, R    = ball_edges
    walls_hit       = ''
    if Up < 0:      walls_hit += 'N'
    if Dn > 1:      walls_hit += 'S'
    if L  < 0:      walls_hit += 'W'
    if R  > 1:      walls_hit += 'E'
    return walls_hit

def velocity_after_wall_collision(velocity, walls_hit):
    vx, vy = velocity
    if 'N' in walls_hit:    vy = vy * -1
    if 'S' in walls_hit:    vy = vy * -1
    if 'E' in walls_hit:    vx = vx * -1
    if 'W' in walls_hit:    vx = vx * -1
    return (vx, vy)

def new_position(position, velocity):
    x, y = position
    dx, dy = velocity
    return (x+dx, y+dy)

def ball_collision(Axy, Ar, Bxy, Br):
    if type(Ar) is tuple:   Ar, Ar = Ar
    else:                   Ar     = Ar
    if type(Br) is tuple:   Br, Br = Br
    else:                   Br     = Br

    Ax, Ay = Axy
    Bx, By = Bxy
    radius_sum_sqd  = (Ar + Br) ** 2
    distance_sqd    = (Ax - Bx) ** 2 + (Ay - By) ** 2
    if distance_sqd < radius_sum_sqd:   return True
    else:                               return False
    
def ball_text_position(text, font, ball_position, window_size):
    fontsize = Coordinate(font.size(text), window_size)
    fontw, fonth = fontsize.abs
    ballx, bally = ball_position
    fontx, fonty = (ballx - fontw//2), (bally - fonth//2)
    return fontx, fonty

def velocity_after_ball_collision(ball_A, ball_B):
    
    def dot_product(vector_1, vector_2):
        x, y = vector_1
        X, Y = vector_2
        return x * X + y * Y
    
    x1, y1 = ball_A.position
    x2, y2 = ball_B.position
    v1 = ball_A.velocity
    v2 = ball_B.velocity
    try:
        m1 = ball_A.mass
    except AttributeError:
        m1 = 1
    try:
        m2 = ball_B.mass
    except AttributeError:
        m2 = 1
    n = x1 - x2, y1 - y2  # normal vector
    n_mag = math.sqrt(n[0] ** 2 + n[1] ** 2)  # magnitude of normal vector
    un = n[0] / n_mag, n[1] / n_mag  # unit vector of n
    ut = -1 * un[1], un[0]  # unit tangent vector of n
    v1n = dot_product(un, v1)
    v1t = dot_product(ut, v1)
    v2n = dot_product(un, v2)
    v2t = dot_product(ut, v2)
    v1t_ = v1t
    v2t_ = v2t
    v1n_ = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2)
    v2n_ = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2)
    v1n__ = (un[0] * v1n_, un[1] * v1n_)
    v1t__ = (ut[0] * v1t_, ut[1] * v1t_)
    v2n__ = (un[0] * v2n_, un[1] * v2n_)
    v2t__ = (ut[0] * v2t_, ut[1] * v2t_)
    
    _v1_ = v1n__[0] + v1t__[0], v1n__[1] + v1t__[1]
    _v2_ = v2n__[0] + v2t__[0], v2n__[1] + v2t__[1]
    
    _v1_ = round(_v1_[0]), round(_v1_[1])
    _v2_ = round(_v2_[0]), round(_v2_[1])
    return (_v1_, _v2_)
