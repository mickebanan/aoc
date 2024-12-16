import heapq

data = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip().splitlines()
data = open('data/16.dat').read().strip().splitlines()
start = next((y, x) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == 'S')
end = next((y, x) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == 'E')
dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
possible_moves = {
    '>': ('>', '^', 'v'),
    '<': ('<', 'v', '^'),
    'v': ('v', '>', '<'),
    '^': ('^', '<', '>'),
}
p1 = []
visited = set()
h = []
heapq.heappush(h, (0, start, '>', tuple()))
while h:
    length, (y, x), moving, path = heapq.heappop(h)
    visited.add((y, x, moving))
    if (y, x) == end:
        p1.append((length, path))
    for move in possible_moves[moving]:
        dy, dx = dirs[move]
        if data[y + dy][x + dx] != '#' and (y + dy, x + dx, move) not in visited:
            new_length = length + 1 if move == moving else length + 1001
            heapq.heappush(h, (new_length, (y + dy, x + dx), move, path + ((y + dy, x + dx),)))

min_p1 = min(length for length, _ in p1)
print('part 1:', min_p1)
best = {start, end}
for length, path in p1:
    if length == min_p1:
        best |= set(path)
print('part 2:', len(best))