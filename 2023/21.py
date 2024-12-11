data = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""
rocks = set()
start = None
data = open('input/21.dat').read()
data = data.strip().split('\n')
ymax = len(data)
xmax = len(data[0])
for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c == '#':
            rocks.add((y, x))
        elif c == 'S':
            start = (y, x)


def move(y, x):
    for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
        if (yy % ymax, xx % xmax) not in rocks:
            yield yy, xx


steps = 26501365
cycle = steps % ymax
copies = steps // ymax
datapoints = []
positions = {start}
p1 = 0
for step in range(steps):
    if step == 64:
        p1 = len(positions)
    new_positions = set()
    for pos in positions:
        for m in move(*pos):
            new_positions.add(m)
    positions = new_positions
    if (step + 1) % ymax == cycle:
        datapoints.append(len(positions))
        if len(datapoints) == 3:
            break
print('part 1:', p1)

# Ended up calculating the part 2 result through a Lagrange interpolation.
# The basic idea is if we know some data points and the rate of expansion,
# we can calculate the value at some specific point in the future,
# as long as the expansion continues in the same way.
# In this case, the data points are picked from the first three cycles
# (namely every 26501365 % 131 steps), then extended out to the full 202300
# copies of that cycle.
# I can't take credit for the calculation, I had to resort to Reddit for help.
# This particular solution may or may not come from here:
# https://github.com/thomasjevskij/advent_of_code/blob/master/2023/aoc21/day21.py
y0, y1, y2 = datapoints
a = (y2 - 2 * y1 + y0) // 2
b = y1 - y0 - a
c = y0
print('part 2:', a * copies**2 + b * copies + c)
