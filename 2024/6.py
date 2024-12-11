data = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip().split('\n')
data = open('data/6.dat').read().strip().split('\n')
ymax = len(data) - 1
xmax = len(data[0]) - 1

def move(data):
    pos = next((y, x) for y, row in enumerate(data) for x, c in enumerate(row) if c in '^v<>')
    visited = {pos}
    direction = data[pos[0]][pos[1]]
    visited_with_direction = {(pos, direction)}
    loop_found = False
    while True:
        y, x = pos
        match direction:
            case '^':
                y -= 1
                new_direction = '>'
            case 'v':
                y += 1
                new_direction = '<'
            case '<':
                x -= 1
                new_direction = '^'
            case _:
                x += 1
                new_direction = 'v'
        if y < 0 or y > ymax or x < 0 or x > xmax:
            break
        elif data[y][x] in '#O':
            direction = new_direction
        else:
            visited.add((y, x))
            if (y, x, direction) in visited_with_direction:
                loop_found = True
                break
            visited_with_direction.add((y, x, direction))
            pos = y, x
    return visited, loop_found

visited, _ = move(data)
print('part 1:', len(visited))

p2 = 0
for y, x in visited:
    d = data.copy()
    if d[y][x] != '.':
        continue
    d[y] = d[y][:x] + 'O' + d[y][x + 1:]
    _, loop_found = move(d)
    if loop_found:
        p2 += 1
print('part 2:', p2)
