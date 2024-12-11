data = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....',
]
with open('11.dat') as f:
    data = [row.strip() for row in f.readlines()]


def transpose(m):
    _m = []
    for i in range(len(m[0])):
        r = []
        for row in m:
            r.append(row[i])
        _m.append(''.join(r))
    return _m


def expand(data):
    empty = set()
    for y, row in enumerate(data):
        if not any(1 for c in row if c == '#'):
            empty.add(y)
    return empty


# expand
empty_ys = expand(data)
data = transpose(data)
empty_xs = expand(data)
data = transpose(data)
galaxies = {(y, x) for y, row in enumerate(data) for x, c in enumerate(row) if c == '#'}


def get_distances(galaxy, part_1=True):
    def get_distance(y1, x1, y2, x2):
        ydiff = xdiff = 0
        if part_1:
            empty_space = 1
        else:
            empty_space = 999_999
        for ey in empty_ys:
            if y1 < ey < y2 or y2 < ey < y1:
                ydiff += empty_space
        for ex in empty_xs:
            if x1 < ex < x2 or x2 < ex < x1:
                xdiff += empty_space
        return abs(y2 - y1) + abs(x2 - x1) + ydiff + xdiff
    return sum(get_distance(*galaxy, *g2) for g2 in galaxies if g2 != galaxy)


print('part 1:', sum(get_distances(g) for g in galaxies) // 2)
print('part 2:', sum(get_distances(g, part_1=False) for g in galaxies) // 2)
