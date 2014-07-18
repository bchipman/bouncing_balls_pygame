def edge_values(position, radius):
    x, y = position
    if type(radius) is tuple:
        r, r = radius
    else:
        r = radius
    U = y - r
    D = y + r
    L = x - r
    R = x + r
    return (U, D, L, R)
def wall_collision(ball, window):
    Up, Dn, L, R = ball.edges
    if Up < 0:
        return True
    if Dn > 1:
        return True
    if L < 0:
        return True
    if R > 1:
        return True
    return False
def wall_hit(ball, window):
    Up, Dn, L, R = ball.edges
    if Up < 0:
        return 'NS'
    if Dn > 1:
        return 'NS'
    if L < 0:
        return 'EW'
    if R > 1:
        return 'EW'
def walls_hit(ball_edges, window_size):
    Up, Dn, L, R = ball_edges
    max_width, max_height = window_size
    walls_hit = ''
    if Up < 0:
        walls_hit += 'N'
    if Dn > max_height:
        walls_hit += 'S'
    if L < 0:
        walls_hit += 'W'
    if R > max_width:
        walls_hit += 'E'
    return walls_hit
def velocity_after_wall_collision_v0(ball, wall):
    vx, vy = ball.velocity
    if wall == 'NS':
        vy = vy * -1
    if wall == 'EW':
        vx = vx * -1
    return (vx, vy)
def velocity_after_wall_collision(velocity, walls_hit):
    vx, vy = velocity
    if 'N' in walls_hit:
        vy = vy * -1
    if 'S' in walls_hit:
        vy = vy * -1
    if 'E' in walls_hit:
        vx = vx * -1
    if 'W' in walls_hit:
        vx = vx * -1
    return (vx, vy)
