data = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""
p1 = []
p2 = []
dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
data = open('input/18.dat').read()
for row in data.strip().split('\n'):
    d, s, h = row.split()
    p1.append((d, int(s)))
    hl, hd = h[2:7], h[7]
    p2.append((dirs[hd], int(hl, 16)))


def make_grid(instructions):
    pos = (0, 0)
    points = [pos]
    perimeter = 0
    for direction, steps in instructions:
        cur_y, cur_x = pos
        perimeter += steps
        match direction:
            case 'R':
                pos = (cur_y, cur_x + steps)
            case 'U':
                pos = (cur_y - steps, cur_x)
            case 'L':
                pos = (cur_y, cur_x - steps)
            case 'D':
                pos = (cur_y + steps, cur_x)
        points.append(pos)
    return points, perimeter


def area(points):
    # shoelace implementation
    area = 0
    q = points[-1]
    for p in points:
        area += p[0] * q[1] - p[1] * q[0]
        q = p
    return area / 2


for name, data in zip(('part 1', 'part 2'), (p1, p2)):
    points, perimeter = make_grid(data)
    a = area(points)
    # pick's theorem
    boundary_area = perimeter / 2 + 1
    print('%s: %s' % (name, int(a + boundary_area)))
