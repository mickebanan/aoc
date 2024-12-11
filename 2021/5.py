import re

import helpers

data = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2',
]
with open('5.dat') as f:
    data = [row.strip() for row in f.readlines()]
xmin = ymin = 0
xmax = ymax = 1000


def viz(grid):
    for row in grid:
        for col in row:
            print(col or '.', end='')
        print()


@helpers.timer
def vents(part_2=False):
    grid = []
    for y in range(ymax):
        grid.append([0] * xmax)
    for row in data:
        m = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', row)
        x1, y1, x2, y2 = m.groups()
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                grid[y1][x] += 1
        elif x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                grid[y][x1] += 1
        elif part_2:
            xrange = range(x1, x2 + 1)
            yrange = range(y1, y2 + 1)
            if x1 > x2:
                xrange = range(x1, x2 - 1, -1)
            if y1 > y2:
                yrange = range(y1, y2 - 1, -1)
            for y, x in zip(yrange, xrange):
                grid[y][x] += 1
    return sum(1 for row in grid for value in row if value > 1)


print('part 1:', vents())
print('part 2:', vents(part_2=True))
