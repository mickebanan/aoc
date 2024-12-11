data = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip().split('\n')
data = open('data/10.dat').read().strip().split('\n')
ymax = len(data) - 1
xmax = len(data[0]) - 1
heads = ((y, x) for y, row in enumerate(data) for x, c in enumerate(row) if c == '0')

def get_value(y, x):
    if data[y][x] != '.':
        return int(data[y][x])
    return -1

def walk(y, x):
    def go(yy, xx):
        if get_value(yy, xx) == value + 1:
            yield yy, xx
    value = int(data[y][x])
    if y < ymax:
        yield from go(y + 1, x)
    if y > 0:
        yield from go(y - 1, x)
    if x < xmax:
        yield from go(y, x + 1)
    if x > 0:
        yield from go(y, x - 1)

p1 = p2 = 0
for head in heads:
    stop = set()
    h = [head]
    while h:
        y, x = h.pop(0)
        for yy, xx in walk(y, x):
            if get_value(yy, xx) == 9:
                stop.add((yy, xx))
                p2 += 1
            else:
                h.append((yy, xx))
    p1 += len(stop)
print('part 1:', p1)
print('part 2:', p2)