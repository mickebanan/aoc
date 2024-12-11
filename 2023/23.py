import sys
from collections import defaultdict

from helpers import timer

data = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""
data = open('input/23.dat').read()
data = list(data.strip().splitlines())
start = (0, 1)
end = (len(data) - 1, data[-1].find('.'))
ymax = len(data)
sys.setrecursionlimit(10000)


def move(y, x, part=1):
    match data[y][x], part:
        # for part 1
        case '>', 1:
            yield y, x + 1
        case '<', 1:
            yield y, x - 1
        case '^', 1:
            yield y - 1, x
        case 'v', 1:
            yield y + 1, x
        case _, _:
            for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                try:
                    if data[yy][xx] != '#' and 0 < yy < ymax:
                        yield yy, xx
                except IndexError:
                    pass


def part1(pos, prev, end, dist):
    if pos == end:
        yield dist
    for m in move(*pos):
        if not prev or m != prev:
            yield from part1(m, pos, end, dist + 1)


def graph(start, end):
    g = defaultdict(list)
    visited = {start}
    q = [(start, start, visited)]
    while q:
        node, prev, visited = q.pop()
        steps = len(visited) - 1
        if node == end:
            g[prev].append((node, steps))
            g[node].append((prev, steps))
            continue
        nn = list(move(*node, part=2))
        nn = [n for n in nn if n not in visited]
        if len(nn) == 1:
            q.append((nn[0], prev, visited | {nn[0]}))
        elif len(nn) > 1:
            if (node, steps) in g[prev]:
                continue
            g[prev].append((node, steps))
            g[node].append((prev, steps))
            for n in nn:
                q.append((n, node, {node, n}))
    return g


@timer
def part2(graph):
    s = 0
    q = [(start, 0, {start})]
    while q:
        node, steps, visited = q.pop()
        if node == end:
            s = max(s, steps)
            continue
        for nn, dist in graph[node]:
            if nn not in visited:
                q.append((nn, steps + dist, visited | {nn}))
    return s


print('part 1:', max(p for p in part1(start, None, end, 0)))
print('part 2:', part2(graph(start, end)))
