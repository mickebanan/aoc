import collections
import re

data = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]
with open('input/3.dat') as f:
    data = [row.strip() for row in f.readlines()]

max_y = len(data) - 1
max_x = len(data[0]) - 1


def check_adjacent(y, x, len, gear=False):
    area = [(y - 1, _x) for _x in range(x - 1, x + len + 2)]
    area += [(y + 1, _x) for _x in range(x - 1, x + len + 2)]
    area += [(y, x - 1), (y, x + len + 1)]
    for y, x in area:
        if y < 0 or y > max_y:
            continue
        if x < 0 or x > max_x:
            continue
        val = data[y][x]
        if not gear:  # part 1
            if not val.isnumeric() and val != '.':
                return True
        else:  # part 2
            if val == '*':
                return y, x


s1 = s2 = 0
gears = collections.defaultdict(list)
for y, row in enumerate(data):
    for m in re.finditer(r'(\d+)', row):
        if check_adjacent(y, m.span()[0], m.span()[1] - m.span()[0] - 1):
            s1 += int(m[0])
        if gear := check_adjacent(y, m.span()[0], m.span()[1] - m.span()[0] - 1, gear=True):
            gears[gear].append(m[0])

for c, values in gears.items():
    if len(values) > 1:
        s2 += int(values[0]) * int(values[1])
# part 1
print(s1)
# part 2
print(s2)
