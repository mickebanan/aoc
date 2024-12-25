import collections
import itertools

data = """
.#..#
.....
#####
....#
...##
""".strip().splitlines()
ymax = len(data) - 1
xmax = len(data[0]) - 1
asteroids = set((y, x) for y, row in enumerate(data) for x, c in enumerate(row) if c == '#')

def scan(y, x, space):
    others = asteroids - {(y, x)}
    space = space[:]
    print('this:', y, x)
    for other in sorted(others, key=lambda v: (abs(y - v[0]) + abs(x - v[1]))):
        dy = yy = other[0] - y
        dx = xx = other[1] - x
        print('other:', other, dy, dx)
        c = 0
        while True:
            c += 1
            if dy == dx:
                yy += 1
                xx += 1
            else:
                yy += dy
                xx += dx
            print('update:', yy, xx)
            if not (0 <= yy <= ymax and 0 <= xx <= xmax):
                break
            space[yy] = space[yy][:xx] + '.' + space[yy][xx + 1:]
            if c > 5:
                break
    print('\n'.join(space))
    c = collections.Counter(''.join(space))
    print(c['#'] - 1)
    return c['#'] - 1

for asteroid in ((2, 4),):
    scan(asteroid[0], asteroid[1], data)