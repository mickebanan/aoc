data = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".strip().split('\n\n')
data = open('data/15.dat').read().strip().split('\n\n')
grid, moves = data
grid_orig = grid[:]
walls = set()
boxes = set()
robot = None
ymax = xmax = 0
dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
for y, row in enumerate(grid.splitlines()):
    ymax = max(ymax, y)
    for x, c in enumerate(row):
        xmax = max(xmax, x)
        match c:
            case '#':
                walls.add((y, x))
            case 'O':
                boxes.add((y, x))
            case '@':
                robot = (y, x)

def push_p1(y, x, dy, dx, boxes):
    found = False
    n = (y + dy, x + dx)
    while not found:
        if n not in walls and n not in boxes:
            found = True
            break
        if n in walls:
            break
        n = (n[0] + dy, n[1] + dx)
    if found:
        ranges = {
            (0, 1): (range(y, y + 1), range(n[1], x - 1, -1)),
            (0, -1): (range(y, y + 1), range(n[1], x + 1)),
            (1, 0): (range(n[0], y - 1, -1), range(x, x + 1)),
            (-1, 0): (range(n[0], y + 1), range(x, x + 1)),
        }
        yrange, xrange = ranges[(dy, dx)]
        for yy in yrange:
            for xx in xrange:
                if (yy, xx) in boxes:
                    boxes.remove((yy, xx))
                    boxes.add((yy + dy, xx + dx))
        return (y + dy, x + dx), boxes
    return (y, x), boxes

for move in moves.replace('\n', ''):
    y, x = robot
    dy, dx = dirs[move]
    if (y + dy, x + dx) in walls:
        continue
    if (y + dy, x + dx) in boxes:
        robot, boxes = push_p1(*robot, dy, dx, boxes)
    else:
        robot = (y + dy, x + dx)
print('part 1:', sum(100 * y + x for y, x in boxes))

def viz():
    print('\n'.join(''.join(row) for row in grid))

def push_p2(y, x, dy, dx, grid):
    if dx == 1:
        next_free = next(((y, n) for n in range(x + 1, xmax) if grid[y][n] == '.'), None)
        if next_free and not any(1 for c in grid[y][x:next_free[1]] if c == '#'):
            boxes = (next_free[1] - x - 1) // 2
            grid[y] = grid[y][:x] + ['.', '@'] + ['[', ']'] * boxes + grid[y][x + 2 + 2*boxes:]
    elif dx == -1:
        next_free = next(((y, n) for n in range(x, -1, -1) if grid[y][n] == '.'), None)
        if next_free and not any(1 for c in grid[y][next_free[1]:x] if c == '#'):
            boxes = (x - next_free[1] - 1) // 2
            grid[y] = grid[y][:x - 2*boxes - 1] + ['[', ']'] * boxes + ['@', '.'] + grid[y][x + 1:]
    elif dy != 0:
        to_check = [(y + dy, x)]
        visited = set()
        can_move = True
        boxes = set()
        while to_check:
            ny, nx = to_check.pop(0)
            boxes.add((ny, nx) if grid[ny][nx] in 'O[' else (ny, nx - 1))
            visited.add((ny, nx))
            for c, dnx in (('[', 1), (']', -1)):
                if grid[ny][nx] == c and (ny, nx + dnx) not in to_check and (ny, nx + dnx) not in visited:
                    to_check.append((ny, nx + dnx))
            if grid[ny + dy][nx] == '#':
                can_move = False
                break
            elif grid[ny + dy][nx] in 'O[]':
                to_check.append((ny + dy, nx))
        if can_move:
            for ny, nx in sorted(boxes, reverse=True if dy == 1 else False):
                grid[ny] = grid[ny][:nx] + ['.', '.'] + grid[ny][nx + 2:]
                grid[ny + dy] = grid[ny + dy][:nx] + ['[', ']'] + grid[ny + dy][nx + 2:]
            pos = grid[y].index('@')
            grid[y][pos] = '.'
            grid[y + dy][pos] = '@'
    return grid

def enlarge(row):
    return row.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')

grid = [list(enlarge(a)) for a in grid_orig.split('\n')]
ymax = len(grid) - 1
xmax = len(grid[0]) - 1

for move in moves.replace('\n', ''):
    dy, dx = dirs[move]
    y, x = next((y, x) for y in range(ymax) for x in range(xmax) if grid[y][x] == '@')
    if grid[y + dy][x + dx] == '#':
        continue
    if grid[y + dy][x + dx] in 'O[]':
        grid = push_p2(y, x, dy, dx, grid)
    else:
        grid[y][x] = '.'
        grid[y + dy][x + dx] = '@'

print('part 2:', sum((y * 100 + x) for y in range(ymax) for x in range(xmax) if grid[y][x] == '['))