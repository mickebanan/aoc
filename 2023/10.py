data = [
    '.....',
    '.S-7.',
    '.|.|.',
    '.L-J.',
    '.....',
]
data = [
    '-L|F7',
    '7S-7|',
    'L|7||',
    '-L-J|',
    'L|-JF',
]
data = [
    '7-F7-',
    '.FJ|7',
    'SJLL7',
    '|F--J',
    'LJ.LJ',
]
data = [
    '...........',
    '.S-------7.',
    '.|F-----7|.',
    '.||.....||.',
    '.||.....||.',
    '.|L-7.F-J|.',
    '.|..|.|..|.',
    '.L--J.L--J.',
    '...........',
]
# data = [
#     '.F----7F7F7F7F-7....',
#     '.|F--7||||||||FJ....',
#     '.||.FJ||||||||L7....',
#     'FJL7L7LJLJ||LJ.L-7..',
#     'L--J.L7...LJS7F-7L7.',
#     '....F-J..F7FJ|L7L7L7',
#     '....L7.F7||L7|.L7L7|',
#     '.....|FJLJ|FJ|F7|.LJ',
#     '....FJL-7.||.||||...',
#     '....L---J.LJ.LJLJ...',
# ]
# data = [
#     'FF7FSF7F7F7F7F7F---7',
#     'L|LJ||||||||||||F--J',
#     'FL-7LJLJ||||||LJL-77',
#     'F--JF--7||LJLJ7F7FJ-',
#     'L---JF-JLJ.||-FJLJJ7',
#     '|F|F-JF---7F7-L7L|7|',
#     '|FFJF7L7F-JF7|JL---7',
#     '7-L-JL7||F7|L7F-7F7|',
#     'L.L7LFJ|||||FJL7||LJ',
#     'L7JLJL-JLJLJL--JLJ.L',
# ]
with open('input/10.dat') as f:
    data = [row.strip() for row in f.readlines()]
h_right = '-7J'
h_left = '-LF'
v_up = '|F7'
v_down = '|JL'


def viz(data):
    for row in data:
        for c in row:
            print(c, end='')
        print()


def get_start():
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == 'S':
                return y, x


def get_next(y, x):
    # The inputs are strings so negative indexes are fine.
    # The structure is a loop so wraparound is not a problem.
    if (y, x) == start:
        if data[y - 1][x] in v_up:
            yield y - 1, x
        if data[y + 1][x] in v_down:
            yield y + 1, x
        if data[y][x - 1] in h_left:
            yield y, x - 1
        if data[y][x + 1] in h_right:
            yield y, x + 1
    else:
        v = data[y][x]
        if v in v_down and data[y - 1][x] in v_up:
            yield y - 1, x
        if v in v_up and data[y + 1][x] in v_down:
            yield y + 1, x
        if v in h_right and data[y][x - 1] in h_left:
            yield y, x - 1
        if v in h_left and data[y][x + 1] in h_right:
            yield y, x + 1


start = get_start()

# part 1
to_visit = {start}
dist = 0
loop = set()
while to_visit:
    n = to_visit.pop()
    if n not in loop:
        loop.add(n)
        dist += 1
        for nn in get_next(*n):
            to_visit.add(nn)
# The halfway point is half of the total length of the loop, rounded up.
print('part 1:', dist // 2)

# part 2
_data = []
for y, row in enumerate(data):
    # Strip out everything not part of the loop.
    _data.append(''.join(data[y][x] if (y, x) in loop else ' ' for x in range(len(row))))
data = _data

_data = []
inside = 0
# It would be enough to just increment the inside counter, the string handling stuff is just for visualization.
for y, row in enumerate(data):
    r = ''
    for x, c in enumerate(row):
        if c == ' ':
            if row[x:].rstrip() == '':
                continue  # don't consider whitespace at the end
            cnt = 0
            for xx in range(x):
                if data[y][xx] in v_up:
                    cnt += 1
            if cnt % 2 == 1:
                # If the amount of vertical pipes to the left is odd, we're inside.
                # If they were even, it would be a loop segment that goes back up,
                # meaning we can't be inside.
                r += 'x'
                inside += 1
            else:
                r += ' '
        else:
            r += c
    _data.append(r)

viz(_data)
print('part 2:', inside)
