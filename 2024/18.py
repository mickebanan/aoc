data = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip().splitlines()
data = open('data/18.dat').read().strip().splitlines()
data = iter(tuple(map(int, row.split(','))) for row in data)
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
start = (0, 0)
end = (6, 6)
end = (70, 70)
ymax = xmax = end[0]
corrupted = set()
for i in range(1024 if end[0] == 70 else 12):
    x, y = next(data)
    corrupted.add((y, x))

def walk():
    q = [(0, start)]
    visited = set()
    while q:
        length, (y, x) = q.pop(0)
        if (y, x) in visited:
            continue
        if (y, x) == end:
            return length
        visited.add((y, x))
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny <= ymax and 0 <= nx <= xmax and (ny, nx) not in corrupted:
                q.append((length + 1, (ny, nx)))
    return None
print('part 1:', walk())

while True:
    cx, cy = next(data)
    corrupted.add((cy, cx))
    v = walk()
    if v is None:
        print('part 2: %s,%s' % (cx, cy))
        break