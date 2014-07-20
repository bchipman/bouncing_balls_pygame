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
