import collections
import itertools

data = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip().split('\n')
data = open('data/8.dat').read().strip().split('\n')
nodes = collections.defaultdict(set)
antinodes = set()
antinodes_p2 = set()
ymax = len(data) - 1
xmax = len(data[0]) - 1
for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c != '.':
            nodes[c].add((y, x))

def get_antinodes(y1, x1, y2, x2, part_1=True):
    def get_next(y, x, dy, dx):
        y, x = y + dy, x + dx
        while 0 <= y <= ymax and 0 <= x <= xmax:
            yield y, x
            if part_1:
                break
            y, x = y + dy, x + dx
    y_here, x_here = y1 - y2, x1 - x2
    y_there, x_there = y2 - y1, x2 - x1
    yield from get_next(y1, x1, y_here, x_here)
    yield from get_next(y2, x2, y_there, x_there)

for node, pos in nodes.items():
    for (y1, x1), (y2, x2) in itertools.combinations(pos, 2):
        antinodes_p2.add((y1, x1))
        antinodes_p2.add((y2, x2))
        for y, x in get_antinodes(y1, x1, y2, x2):
            antinodes.add((y, x))
        for y, x in get_antinodes(y1, x1, y2, x2, part_1=False):
            antinodes_p2.add((y, x))
print('part 1:', len(antinodes))
print('part 2:', len(antinodes_p2))
