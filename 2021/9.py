import bisect
import operator
from functools import reduce

data = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678',
]
with open('9.dat') as f:
    data = [row.strip() for row in f.readlines()]
low_points = []
ymax = len(data) - 1
xmax = len(data[0]) - 1


def check(y, x, value):
    for yy, xx in get_neighbors(y, x):
        if data[yy][xx] <= value:
            return False
    return True


def get_neighbors(y, x):
    if x:
        yield y, x - 1
    if x < xmax:
        yield y, x + 1
    if y:
        yield y - 1, x
    if y < ymax:
        yield y + 1, x


risk = 0
basins = set()
for y, row in enumerate(data):
    for x, value in enumerate(row):
        if check(y, x, value):
            basins.add((y, x))
            risk += 1 + int(value)
print('part 1:', risk)

basin_sizes = []
for basin in basins:
    to_visit = {basin}
    b = set()
    while to_visit:
        v = to_visit.pop()
        if v not in b:
            b.add(v)
            for y, x in get_neighbors(v[0], v[1]):
                if data[y][x] < '9':
                    to_visit.add((y, x))
    bisect.insort(basin_sizes, len(b))
    basin_sizes = basin_sizes[-3:]
print('part 2:', reduce(operator.mul, basin_sizes))
