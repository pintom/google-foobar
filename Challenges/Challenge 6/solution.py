from collections import deque


def inside(n, maze):
    return 0 <= n[0] < len(maze) and 0 <= n[1] < len(maze[0])


def n_walls(p, maze):
    return sum([maze[n[0]][n[1]] for n in p])


steps = ((0, 1), (0, -1), (1, 0), (-1, 0))


def next_steps(p, maze):
    nodes = [(p[-1][0] + dp[0], p[-1][1] + dp[1]) for dp in steps]
    paths = [p + [tuple(n)] for n in nodes if inside(n, maze) and n not in p]
    return [p for p in paths if n_walls(p, maze) <= 1]


def overlap(p0, p1, maze):
    return any(p0[-1] in p and n_walls(p0, maze) >= n_walls(p, maze) for p in p1)


def answer(maze):
    p1 = deque([[(0, 0)]])
    g = (len(maze) - 1, len(maze[0]) - 1)
    while True:
        new_p = [p for p in next_steps(p1.pop(), maze) if not overlap(p, p1, maze)]
        if any(p[-1] == g for p in new_p):
            p1 = new_p
            break
        p1.extendleft(new_p)
    for p in p1:
        if p[-1] == g:
            return len(p)
