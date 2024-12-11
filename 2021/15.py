import heapq

import helpers

data = [
    '1163751742',
    '1381373672',
    '2136511328',
    '3694931569',
    '7463417111',
    '1319128137',
    '1359912421',
    '3125421639',
    '1293138521',
    '2311944581',
]
with open('15.dat') as f:
    data = [row.strip() for row in f.readlines()]
orig_ymax = len(data) - 1
orig_xmax = len(data[0]) - 1
ymax = len(data) * 5 - 1
xmax = len(data[0]) * 5 - 1
start = (0, 0)


def get_value(y, x, part_1=True):
    if part_1:
        return int(data[y][x])
    xx = x % (orig_xmax + 1)
    yy = y % (orig_ymax + 1)
    v = int(data[yy][xx])
    diff_y = y // (orig_ymax + 1)
    diff_x = x // (orig_xmax + 1)
    v += diff_y + diff_x
    return v - 9 if v > 9 else v


def get_neighbors(y, x, part_1=True):
    if x:
        yield y, x - 1
    if x < (orig_xmax if part_1 else xmax):
        yield y, x + 1
    if y:
        yield y - 1, x
    if y < (orig_ymax if part_1 else ymax):
        yield y + 1, x


@helpers.timer
def walk(pos, end, part_1=True):
    distances = {}
    hq = []
    unvisited = set()
    for y in range((orig_ymax if part_1 else ymax) + 1):
        for x in range((orig_xmax if part_1 else xmax) + 1):
            n = (y, x)
            distances[n] = 1e6
            unvisited.add(n)
    distances[pos] = 0
    heapq.heappush(hq, (0, pos))
    while unvisited:
        u = heapq.heappop(hq)[1]
        if u == end:
            return distances[end]
        unvisited.remove(u)
        for nn in get_neighbors(*u, part_1=part_1):
            if nn in unvisited:
                alt = distances[u] + get_value(*nn, part_1=part_1)
                if alt < distances[nn]:
                    distances[nn] = alt
                    heapq.heappush(hq, (alt, nn))


def p1():
    end = (orig_ymax, orig_xmax)
    d = walk(start, end)
    print('part 1:', d)


def p2():
    end = (ymax, xmax)
    d = walk(start, end, part_1=False)
    print('part 2:', d)


p1()
p2()
