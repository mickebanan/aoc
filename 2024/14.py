import collections
import copy

data = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip().splitlines()
data = open('data/14.dat').read().splitlines()
tiles = collections.defaultdict(set)
for entry in data:
    p, v = entry.split()
    x, y = map(int, p.replace('p=', '').split(','))
    dx, dy = map(int, v.replace('v=', '').split(','))
    tiles[(y, x)].add((dy, dx))
tiles_orig = copy.deepcopy(tiles)
ymax = 103
xmax = 101

def viz(tiles):
    for y in range(ymax):
        for x in range(xmax):
            print('#', end='') if (y, x) in tiles else print(' ', end='')
        print()

def move(tiles, steps=1):
    d = collections.defaultdict(set)
    for (y, x), robots in tiles.items():
        for dy, dx in robots:
            d[((y + dy * steps) % ymax, (x + dx * steps) % xmax)].add((dy, dx))
    return d

def get_safety_score(tiles):
    q1 = q2 = q3 = q4 = 0
    for y in range(ymax):
        if y == ymax // 2:
            continue
        for x in range(xmax):
            if x == xmax // 2:
                continue
            if (y, x) in tiles:
                if y < ymax // 2 and x < xmax // 2:
                    q1 += len(tiles[(y, x)])
                if y > ymax // 2 and x < xmax // 2:
                    q2 += len(tiles[(y, x)])
                if y < ymax // 2 and x > xmax // 2:
                    q3 += len(tiles[(y, x)])
                if y > ymax // 2 and x > xmax // 2:
                    q4 += len(tiles[(y, x)])
    return q1 * q2 * q3 * q4

tiles_p1 = move(tiles, steps=100)
score = get_safety_score(tiles_p1)
print('part 1:', score)

p2 = 0
for i in range(1, 10000):
    # The assumption is the tree is going to be much more ordered than the regular static,
    # so its safety score should be comparatively lower. Solutions should be checked visually.
    tiles = move(tiles)
    s = get_safety_score(tiles)
    if s < score:
        print(' solution?', i, s)
        score = s
        p2 = i
print('part 2: %s?' % p2)
viz(move(tiles_orig, steps=p2))
