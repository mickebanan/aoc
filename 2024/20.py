import collections

grid = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip().splitlines()
grid = open('data/20.dat').read().strip().splitlines()
start = next((y, x) for y, row in enumerate(grid) for x, c in enumerate(row) if c == 'S')
end = next((y, x) for y, row in enumerate(grid) for x, c in enumerate(row) if c == 'E')
ymax = len(grid) - 1
xmax = len(grid[0]) - 1
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

def run(start, end):
    q = [(0, start)]
    d1 = collections.defaultdict(set)  # map distances to nodes
    d2 = collections.defaultdict(int)  # map nodes to distances
    path = []
    while q:
        length, (y, x) = q.pop(0)
        if (y, x) in path:
            continue
        d1[length].add((y, x))
        d2[(y, x)] = length
        path.append((y, x))
        if (y, x) == end:
            return d1, d2, reversed(path)
        for dy, dx in dirs:
            if 0 <= y + dy <= ymax and 0 <= x + dx <= xmax and grid[y + dy][x + dx] != '#':
                q.append((length + 1, (y + dy, x + dx)))

pos_to_end, length_to_pos, path = run(end, start)
p1 = collections.Counter()
p2 = collections.Counter()
target = 100
for i, pos in enumerate(path):
    curr_dist = length_to_pos[pos]
    y1, x1 = pos
    for j in range(curr_dist - target - 1, -1, -1):
        for y2, x2 in pos_to_end[j]:
            dist = abs(y2 - y1) + abs(x2 - x1)
            if dist == 2 and (length_to_pos[(y2, x2)] + dist) < length_to_pos[pos]:
                p1[curr_dist - j - dist] += 1
            if 2 <= dist <= 20 and (length_to_pos[(y2, x2)] + dist) < length_to_pos[pos]:
                p2[curr_dist - j - dist] += 1

print('part 1:', sum(v for k, v in p1.items() if k >= target))
print('part 2:', sum(v for k, v in p2.items() if k >= target))
