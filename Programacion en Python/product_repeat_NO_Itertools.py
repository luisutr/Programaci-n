from itertools import *


''''#con version 2 
def producto(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
'''

def producto(*args, **kwds):
    "Alternative fast implementation of product for python < 2.6"
    def cycle(sequence, uplevel):
        while True:
            vals = next(uplevel)   # advance upper level, raises if done
            it = iter(sequence)    # (re-)start iteration of current level
            try:
                while True: yield vals + (next(it),)
            except StopIteration:
                pass

    step = iter(((),))
    for pool in map(tuple, args)*kwds.get('repeat', 1):
        step = cycle(pool, step)   # build stack of iterators
    return step

list2=range(4)
print(list(producto(list2,repeat=3)))
print(list(product(list2,repeat=3)))
#product(A, repeat=4) means the same as product(A, A, A, A).
