import heapq

from helpers import timer

data = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
data = """
111111111111
999999999991
999999999991
999999999991
999999999991
"""
data = [d for d in data.strip().splitlines()]
data = [d for d in open('input/17.dat').read().splitlines()]
ymax = len(data) - 1
xmax = len(data[0]) - 1
start = (0, 0)
end = (ymax, xmax)


def get_value(y, x):
    if 0 <= y <= ymax and 0 <= x <= xmax:
        return int(data[y][x])
    return 0


def get_next(y, x, direction, dc):
    if direction == '>':
        if x < xmax:
            yield y, x + 1, '>', dc + 1
        if y:
            yield y - 1, x, '^', 0
        if y < ymax:
            yield y + 1, x, 'v', 0
    if direction == '<':
        if x:
            yield y, x - 1, '<', dc + 1
        if y:
            yield y - 1, x, '^', 0
        if y < ymax:
            yield y + 1, x, 'v', 0
    if direction == '^':
        if y:
            yield y - 1, x, '^', dc + 1
        if x:
            yield y, x - 1, '<', 0
        if x < xmax:
            yield y, x + 1, '>', 0
    if direction == 'v':
        if y < ymax:
            yield y + 1, x, 'v', dc + 1
        if x:
            yield y, x - 1, '<', 0
        if x < xmax:
            yield y, x + 1, '>', 0


@timer
def walk(min_walk=0, max_walk=2):
    hq = []
    heapq.heappush(hq, (0, start, '>', 0))
    heapq.heappush(hq, (0, start, 'v', 0))
    visited = set()
    while hq:
        cost, u, d, dc = heapq.heappop(hq)
        if (u, d, dc) in visited:
            continue
        visited.add((u, d, dc))
        if u == end and dc >= min_walk:
            return cost
        cur_y, cur_x = u
        for yy, xx, next_d, next_dc in get_next(cur_y, cur_x, d, dc):
            if next_dc > max_walk:
                continue
            if dc < min_walk and next_d != d:
                continue
            heapq.heappush(hq, (cost + get_value(yy, xx), (yy, xx), next_d, next_dc))
    return -1


p1 = walk()
print('part 1', p1)
p2 = walk(min_walk=3, max_walk=9)
print('part 2', p2)
