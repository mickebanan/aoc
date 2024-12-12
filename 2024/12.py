data = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip().split('\n')
data = open('data/12.dat').read().strip().split('\n')
ymax = len(data) - 1
xmax = len(data[0]) - 1
unvisited = {(y, x) for y in range(ymax + 1) for x in range(xmax + 1)}
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
convex_edges = (
    ((0, -1), (-1, 0)),  # top left
    ((0, 1), (-1, 0)),  # top right
    ((0, -1), (1, 0)),  # bottom left
    ((0, 1), (1, 0)),  # bottom right
)
concave_edges = (
    ((0, -1), (-1, 0), (-1, -1)),  # top left
    ((0, 1), (-1, 0), (-1, 1)),  # top right
    ((0, -1), (1, 0), (1, -1)),  # bottom left
    ((0, 1), (1, 0), (1, 1)),  # bottom right
)
p1 = p2 = 0

def get(y, x):
    if 0 <= y <= ymax and 0 <= x <= xmax:
        return data[y][x]
    return ''

while unvisited:
    q = [next(iter(unvisited))]
    area = 0
    perimeter = 0
    corners = 0
    while q:
        y, x = q.pop(0)
        area += 1
        perimeter += 4
        unvisited.remove((y, x))
        c = get(y, x)
        for dy, dx in dirs:
            if get(y + dy, x + dx) == c:
                perimeter -= 1
                if (y + dy, x + dx) in unvisited and (y + dy, x + dx) not in q:
                    q.append((y + dy, x + dx))
        for (dy1, dx1), (dy2, dx2) in convex_edges:
            if (get(y + dy1, x + dx1) != c
                    and get(y + dy2, x + dx2) != c):
                corners += 1
        for (dy1, dx1), (dy2, dx2), (dy3, dx3) in concave_edges:
            if (get(y + dy1, x + dx1) == c
                    and get(y + dy2, x + dx2) == c
                    and get(y + dy3, x + dx3) != c):
                corners += 1
    p1 += area * perimeter
    p2 += area * corners
print('part 1:', p1)
print('part 2:', p2)