from collections import deque
from fractions import Fraction
import operator

def contains(small, big):
    for i in xrange(len(big)-len(small)+1):
        for j in xrange(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

def loop_value(l, m):
    x = reduce(operator.mul,
               [Fraction(m[i][j], sum(m[i])) for i, j in zip(l, l[1:]+[l[0]])],
               1)
    return 1/(1-x)

def calculate_loops(p, L, m):
    f = Fraction(1)
    for l in L:
        while True:
            idx = contains(l, p)
            if not idx: break
            f *= loop_value(l, m)
            p = [s for i, s in enumerate(p) if not idx[0] <= i < idx[1]]
    return f

def steps(p, L, m):
    # Find loop, calculate, and add to aggregate for each step
    L.extend(p[p.index(i):] for i, t in enumerate(m[p[-1]]) if t > 0 and i in p)
    return [p+[i] for i, t in enumerate(m[p[-1]]) if t > 0 and i not in p]

def answer(m):
    Sf = {i: Fraction(0) for i, ts in enumerate(m) if not any(ts)}
    P  = deque([0, i] for i, t in enumerate(m[0]) if t > 0)
    Pf = [p for p in P if p[-1] in Sf] # Stable paths
    for p in Pf: P.remove(p)
    L  = [] # Loops
    while P:
        for p in steps(P.pop(), L, m):
            if p[-1] in Sf:
                Pf.append(p)
            else:
                P.appendleft(p)
    for p in Pf:
        Sf[p[-1]] += reduce(operator.mul,
                           [Fraction(m[i][j], sum(m[i])) for i, j in zip(p[:-1], p[1:])],
                           calculate_loops(p, L, m))
    print(Sf)


m1 = [[0, 2, 1, 0, 0],
      [0, 0, 0, 3, 4],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]]
# [7, 6, 8, 21]
m2 = [[0, 1, 0, 0, 0, 1],
      [4, 0, 0, 3, 2, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]]
# [0, 3, 2, 9, 14]

answer(m1)
answer(m2)