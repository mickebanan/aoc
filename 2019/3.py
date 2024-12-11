import math

data = """
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
""".strip().split('\n')
data = open('data/3.dat').read().strip().split('\n')
w1, w2 = data

def walk(wire, until=None):
    pos = (0, 0)
    path = set()
    distance = 0
    for step in wire.split(','):
        direction, length = step[0], step[1:]
        d = {'R': (0, 1), 'U': (1, 0), 'L': (0, -1), 'D': (-1, 0)}[direction]
        for _ in range(int(length)):
            pos = (pos[0] + d[0], pos[1] + d[1])
            path.add(pos)
            distance += 1
            if until and pos == until:
                return distance
    return path

p1 = p2 = 1_000_000
for c in walk(w1) & walk(w2):
    p1 = min(p1, abs(c[0]) + abs(c[1]))
    d = 0
    for w in w1, w2:
        d += walk(w, until=c)
    p2 = min(p2, d)
print('part 1:', p1)
print('part 2:', p2)