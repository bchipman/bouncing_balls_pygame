from collections import namedtuple
import sys
import os
import random
#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------
if __name__ != '__main__':
    change_sys_path()

if __name__ == '__main__':
    change_sys_path()
    print_sys_path()
    import pygame
