__author__ = 'Luis'

def solutions():
    # letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y')
    all_solutions = list()
    for s in range(9, -1, -1):
        for e in range(9, -1, -1):
            for n in range(9, -1, -1):
                for d in range(9, -1, -1):
                    for m in range(9, 0, -1):
                        for o in range(9, -1, -1):
                            for r in range(9, -1, -1):
                                for y in range(9, -1, -1):
                                    if len(set([s, e, n, d, m, o, r, y])) == 8:
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y

                                        if send + more == money:
                                            all_solutions.append((send, more, money))
    return all_solutions

#print(solutions())

from itertools import combinations, permutations

def replacements():
    for comb in combinations(range(10), 8):
        for perm in permutations(comb):
            if perm[0] * perm[1] != 0:
                yield dict(zip('SMENDORY', perm))

a, b, c = 'SEND', 'MORE', 'MONEY'

def criptomatica():
    for replacement in replacements():
        f = lambda x: sum(replacement[e] * 10**i for i, e in enumerate(x[::-1]))
        if f(a) + f(b) == f(c):
            print('{} + {} = {}'.format(f(a), f(b), f(c)))


import time
import itertools


def timeit(fn):
    def wrapper():
        start = time.clock()
        ret = fn()
        elapsed = time.clock() - start
        print("%s took %2.fs" % (fn.__name__, elapsed))
        return ret
    return wrapper


@timeit
def solve1():
    for s in xrange(1, 10):
        for e in xrange(0, 10):
            for n in xrange(0, 10):
                for d in xrange(0, 10):
                    for m in xrange(1, 10):
                        for o in xrange(0, 10):
                            for r in xrange(0, 10):
                                for y in xrange(0, 10):
                                    if distinct(s, e, n, d, m, o, r, y):
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
                                        if send + more == money:
                                            return send, more, money


def distinct(*args):
    return len(set(args)) == len(args)


@timeit
def solve2():
    letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y')
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sol['s'] == 0 or sol['m'] == 0:
            continue
        send = 1000 * sol['s'] + 100 * sol['e'] + 10 * sol['n'] + sol['d']
        more = 1000 * sol['m'] + 100 * sol['o'] + 10 * sol['r'] + sol['e']
        money = 10000 * sol['m'] + 1000 * sol['o'] + 100 * sol['n'] + 10 * sol['e'] + sol['y']
        if send + more == money:
            return send, more, money


#print(solve1())
#print(solve2())


#############Code begins###############

from itertools import permutations

def solve(puzzle):
    """solve alphametic puzzles in just 9 lines of code.
Make sure each operator is seperated from the words by
white-spaces, e.g.:

>>> solve('send + more == money')

"""
    words = [w for w in puzzle.split() if w.isalpha()]
    nonzeros = {w[0] for w in words}
    others = {a for a in ''.join(words) if a not in nonzeros}
    chars = [ord(c) for c in nonzeros]+[ord(c) for c in others]
    assert len(chars) <= 10, 'Too many letters'
    for guess in permutations('0123456789', len(chars)):
        if '0' not in guess[:len(nonzeros)]:
            equation = puzzle.translate(dict(zip(chars, guess)))
            if eval(equation): return puzzle, equation

if __name__ == '__main__':
    print ('\n'.join(solve("send + more == money")))
