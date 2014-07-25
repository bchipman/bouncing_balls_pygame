def edge_values(position, radius):
    x, y = position
    if type(radius) is tuple:   r, r = radius
    else:                       r    = radius
    U = y - r
    D = y + r
    L = x - r
    R = x + r
    return (U, D, L, R)

def walls_hit(ball_edges, window_size):
    Up, Dn, L, R    = ball_edges
    max_w, max_h    = window_size
    walls_hit       = ''
    if Up < 0:          walls_hit += 'N'
    if Dn > max_h:      walls_hit += 'S'
    if L  < 0:          walls_hit += 'W'
    if R  > max_w:      walls_hit += 'E'
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
    Ax, Ay = Axy
    Bx, By = Bxy
    radius_sum_sqd  = (Ar + Br) ** 2
    distance_sqd    = (Ax - Bx) ** 2 + (Ay - By) ** 2
    if distance_sqd < radius_sum_sqd:   return True
    else:                               return False
    
def ball_text_position(text, font, ball_position):
    fontw, fonth = font.size(text)
    ballx, bally = ball_position
    fontx, fonty = (ballx - fontw//2), (bally - fonth//2)
    return fontx, fonty
