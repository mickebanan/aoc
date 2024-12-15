import pprint

data = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".strip().split('\n\n')
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
walls = set()
boxes = set()
robot = None
dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
ymax = xmax = 0
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

def viz():
    for _y in range(ymax + 1):
        for _x in range(xmax + 1):
            if (_y, _x) in walls:
                print('#', end='')
            elif (_y, _x) in boxes:
                print('O', end='')
            elif robot == (_y, _x):
                print('@', end='')
            else:
                print('.', end='')
        print()

def push(y, x, dy, dx, boxes):
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

# print('Initial state:')
# viz()
for move in moves.replace('\n', ''):
    y, x = robot
    dy, dx = dirs[move]
    if (y + dy, x + dx) in walls:
        continue
    if (y + dy, x + dx) in boxes:
        robot, boxes = push(*robot, dy, dx, boxes)
    else:
        robot = (y + dy, x + dx)
print('part 1:', sum(100 * y + x for y, x in boxes))