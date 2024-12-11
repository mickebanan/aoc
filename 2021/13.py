import re

data = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5',
]
with open('13.dat') as f:
    data = [row.strip() for row in f.readlines()]
dots = set()
xmax = ymax = 0
instructions = []
for i, row in enumerate(data):
    if not row:
        continue
    if m := re.match(r'fold along (.+)=(\d+)', row):
        instructions.append((m[1], int(m[2])))
    else:
        x, y = row.split(',')
        x = int(x)
        y = int(y)
        xmax = max(xmax, x)
        ymax = max(ymax, y)
        dots.add((y, x))


def viz():
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            if (y, x) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print()


def fold_y(where):
    global ymax
    for x in range(xmax + 1):
        for y in range(where, ymax + 1):
            if (y, x) in dots:
                dots.add((ymax - y, x))
                dots.remove((y, x))
    ymax = where - 1


def fold_x(where):
    global xmax
    for y in range(ymax + 1):
        for x in range(where, xmax + 1):
            if (y, x) in dots:
                dots.add((y, xmax - x))
                dots.remove((y, x))
    xmax = where - 1


for i, (axis, where) in enumerate(instructions):
    if axis == 'x':
        fold_x(where)
    else:
        fold_y(where)
    if i == 0:
        print('part 1:', len(dots))
print('part 2:')
viz()

