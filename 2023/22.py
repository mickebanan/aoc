from collections import defaultdict

data = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""
data = open('input/22.dat').read()
bricks = []
bricks_below = defaultdict(set)
bricks_above = defaultdict(set)


def sorted_input(v):
    a, _ = v.split('~')
    return int(a.split(',')[-1])


for row in sorted(data.strip().split('\n'), key=sorted_input):
    brick = set()
    c1, c2 = row.split('~')
    c1, c2 = c1.split(','), c2.split(',')
    xrange = {x for x in range(int(c1[0]), int(c2[0]) + 1)}
    yrange = {y for y in range(int(c1[1]), int(c2[1]) + 1)}
    zrange = {z for z in range(int(c1[2]), int(c2[2]) + 1)}
    for z in zrange:
        for y in yrange:
            for x in xrange:
                brick.add((x, y, z))
    bricks.append(brick)


def collapse(bricks):
    def drop(brick, prev_bricks):
        falling = True
        while falling:
            if min(z for (x, y, z) in brick) == 1:
                return brick
            candidate = {(x, y, z - 1) for x, y, z in brick}
            for p in prev_bricks:
                if set(p) & candidate:
                    falling = False
                    bricks_below[tuple(brick)].add(tuple(p))
            if falling:
                brick = candidate
        brick = tuple(brick)
        for below in bricks_below[brick]:
            bricks_above[below].add(brick)
        return brick

    falling_bricks = iter(bricks)
    settled_bricks = []
    while brick := next(falling_bricks, False):
        b = drop(brick, settled_bricks)
        settled_bricks.append(b)
    return settled_bricks


bricks = collapse(bricks)
p1 = p2 = 0
for brick in bricks:
    brick = tuple(brick)
    if b := bricks_above[brick]:
        if all((len(bricks_below.get(a)) > 1 for a in b)):
            p1 += 1
    else:
        p1 += 1
    q = [brick]
    falling_bricks = {brick}
    while q:
        b = q.pop(0)
        for ba in bricks_above.get(b, {}):
            if not bricks_below.get(ba) - falling_bricks:
                falling_bricks.add(ba)
                q.append(ba)
    p2 += len(falling_bricks - {brick})

print('part 1:', p1)
print('part 2:', p2)
