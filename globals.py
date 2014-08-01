#-----------------------------------IMPORTS-------------------------------------
from collections import namedtuple
import sys
import os
import random

#------------------------------GENERIC_FUNCTIONS--------------------------------
def mk_namedtuple(name, di):
    return namedtuple(name, di.keys())(**di)

def print_sys_path():
    for p in sys.path:
        print(repr(p))

def change_sys_path():
    sys.path = sorted(sys.path) # simple list sorting also seems to be effective at removing the import warning

def rnd(range_or_choices):
    if type(range_or_choices) is tuple:
        a, b = range_or_choices
        if type(a) == type(b) == int:
            return random.randint(a, b)
        elif type(a) == type(b) == float:
            return random.uniform(a, b)
    elif type(range_or_choices) is list:
        return random.choice(range_or_choices)     

#-------------------------------GLOBAL_VARIABLES--------------------------------
options = mk_namedtuple('Options', dict(
    total_number_balls  = 10,                   # integer
    center_xy_range     = (0.010,   0.99 ),     # proportion of window
    radius_range        = (0.025,   0.075),     # proportion of window
    velocity_range      = (0.005,   0.010),     # proportion of window
    initial_window_size = (  300,   300  ),     # pixels
    window_pos_desktop  = ( 2200,   150  ),     # pixels
    window_pos_laptop   = ( 1050,   150  ),     # pixels
    font_size           = 24,
    ))  

def font():
    return pygame.font.SysFont(None, options.font_size)

def window_size():
    return pygame.display.get_surface().get_size()

#-----------------------------------__MAIN__------------------------------------
if __name__ != '__main__':
    change_sys_path()
    import pygame
    pygame.init()

if __name__ == '__main__':
    change_sys_path()
    print_sys_path()
    import pygame
#-------------------------------------------------------------------------------
