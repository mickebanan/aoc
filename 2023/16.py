import functools

from helpers import timer

data = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""".strip().split('\n')
data = open('input/16.dat').read().strip().split('\n')
ymax = len(data)
xmax = len(data[0])
mirrors = {
    '\\': {'e': 's', 'w': 'n', 'n': 'w', 's': 'e'},
    '/': {'e': 'n', 'w': 's', 'n': 'e', 's': 'w'}
}


@functools.cache
def shine(pos, direction, path=None):
    if path is None:
        path = tuple()

    def move():
        nonlocal pos
        y, x = pos
        if direction == 'e':
            pos = (y, x + 1)
        elif direction == 'w':
            pos = (y, x - 1)
        elif direction == 'n':
            pos = (y - 1, x)
        elif direction == 's':
            pos = (y + 1, x)

    def get_nodes(path):
        return {p for p, d in path}

    while 0 <= pos[0] < ymax and 0 <= pos[1] < xmax:
        # if (pos, direction) in cache:  # previously traversed
        #     yield get_nodes(path) | cache[(pos, direction)]
        #     break
        if (pos, direction) in path:  # loop detected
            # print('found loop at', pos, direction)
            # i = path.index((pos, direction))
            # cache[(pos, direction)] = get_nodes(path[i:])
            # print(sorted(get_nodes(loop)))
            yield get_nodes(path)
            break
        else:
            path += (pos, direction)
            v = data[pos[0]][pos[1]]
            if v in mirrors:
                direction = mirrors[v][direction]
            elif v == '|' and direction in ('w', 'e'):
                direction = 's'
                yield from shine(pos, 'n', path=tuple(path))
            elif v == '-' and direction in ('n', 's'):
                direction = 'w'
                yield from shine(pos, 'e', path=tuple(path))
            move()
    yield get_nodes(path)


def viz(tiles):
    for y in range(ymax):
        for x in range(xmax):
            print('#' if (y, x) in tiles else '.', end='')
        print()


def p1():
    paths = set()
    for path in shine((11, 109), 'w'):
        paths |= set(path)
    # viz(paths)
    return len(paths)


@timer
def p2():
    cache = {}
    maxtiles = 0
    for y in range(ymax):
        for x, d in zip((0, xmax - 1), ('e', 'w')):
            paths = set()
            for path in shine((y, x), d):
                paths |= path
            # print(paths)
            print(y, x, len(paths))
            if (y, x) == (11, 109):
                viz(paths)
            if len(paths) > maxtiles:
                print(y, x, d)
                # viz(paths)
                maxtiles = max(maxtiles, len(paths))
    for x in range(xmax):
        for y, d in zip((0, ymax - 1), ('s', 'n')):
            paths = set()
            for path in shine((y, x), d):
                paths |= path
            # print(y, x, len(paths))
            if len(paths) > maxtiles:
                # print(y, x, d)
                # viz(paths)
                maxtiles = max(maxtiles, len(paths))
    return maxtiles


# print('part 1:', p1())
print('part 2:', p2())
