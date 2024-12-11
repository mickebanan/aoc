import copy

data = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526',
]
data = [
    '1443582148',
    '6553734851',
    '1451741246',
    '8835218864',
    '1662317262',
    '1731656623',
    '1128178367',
    '5842351665',
    '6677326843',
    '7381433267',
]
# data = [
#     '11111',
#     '19991',
#     '19191',
#     '19991',
#     '11111',
# ]
_data = []
for row in data:
    r = [int(a) for a in row]
    _data.append(r)
data = _data
ymax = len(data) - 1
xmax = len(data[0]) - 1


def viz():
    for row in data:
        print(''.join(str(a) for a in row))


def get_neighbors(y, x):
    if x:
        yield y, x - 1
    if x < xmax:
        yield y, x + 1
    if y:
        yield y - 1, x
    if y < ymax:
        yield y + 1, x
    if x and y:
        yield y - 1, x - 1
    if x < xmax and y:
        yield y - 1, x + 1
    if x and y < ymax:
        yield y + 1, x - 1
    if x < xmax and y < ymax:
        yield y + 1, x + 1


def increment(y, x, data):
    data[y][x] += 1
    return data[y][x]


def work(n, data, part_1=False):
    total_flashes = 0
    for step in range(n):
        flashes_this_turn = 0
        # increase all values
        flashes = set()
        for y, row in enumerate(data):
            for x, _ in enumerate(row):
                value = increment(y, x, data)
                if value > 9:
                    flashes.add((y, x))
        # flashing
        flashed = set()
        while flashes:
            octopus = flashes.pop()
            if octopus not in flashed:
                flashed.add(octopus)
                flashes_this_turn += 1
                for yy, xx in get_neighbors(*octopus):
                    value = increment(yy, xx, data)
                    if value > 9:
                        flashes.add((yy, xx))
        # reset
        for y, x in flashed:
            data[y][x] = 0
        total_flashes += flashes_this_turn
        if flashes_this_turn == 100 and not part_1:
            return step + 1
    return total_flashes


def p1():
    n = work(100, copy.deepcopy(data))
    print('part 1:', n)


def p2():
    turn = work(10000, copy.deepcopy(data), part_1=False)
    print('part 2:', turn)


p1()
p2()

