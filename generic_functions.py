from collections import namedtuple

def mk_namedtuple(name, di):
    return namedtuple(name, di.keys())(**di)

