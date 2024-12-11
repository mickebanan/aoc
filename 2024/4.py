data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".strip().split('\n')
data = open('data/4.dat').read().strip().split('\n')
ymax = len(data) - 1
xmax = len(data[0]) - 1
directions = (
    ((0, 1), (0, 2), (0, 3)),
    ((1, 1), (2, 2), (3, 3)),
    ((1, 0), (2, 0), (3, 0)),
    ((1, -1), (2, -2), (3, -3)),
    ((0, -1), (0, -2), (0, -3)),
    ((-1, -1), (-2, -2), (-3, -3)),
    ((-1, 0), (-2, 0), (-3, 0)),
    ((-1, 1), (-2, 2), (-3, 3)),
)
x_directions = (
    ((-1, -1), (0, 0), (1, 1)),
    ((-1, 1), (0, 0), (1, -1)),
)
p1 = p2 = 0

def check(y, x, combinations=('MAS',), directions=directions, p1=True):
    dirs = {d: False for d in directions}
    for combination in combinations:
        for direction in directions:
            for letter, (dy, dx) in zip(combination, direction):
                yy = y + dy
                xx = x + dx
                if not 0 <= yy <= ymax or not 0 <= xx <= xmax or not data[yy][xx] == letter:
                    break
            else:
                dirs[direction] = True
    if p1:
        return sum(dirs.values())
    return 1 if all(dirs.values()) else 0

for y in range(ymax + 1):
    for x in range(xmax + 1):
        if data[y][x] == 'X':
            if val := check(y, x):
                p1 += val
        elif data[y][x] == 'A':
            if check(y, x, combinations=('SAM', 'MAS'), directions=x_directions, p1=False):
                p2 += 1
print('part 1:', p1)
print('part 2:', p2)
