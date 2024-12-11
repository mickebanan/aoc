import operator
import re
from functools import reduce

data = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]
with open('input/2.dat') as f:
    data = [line.strip() for line in f.readlines()]
data = [row.strip() for row in data]
limit = {'red': 12, 'green': 13, 'blue': 14}

s1 = s2 = 0
for line in data:
    m = re.match(r'Game (\d+): (.*)', line)
    game_id, configuration = m.groups()
    configuration = configuration.split(';')
    possible = True
    # part 1
    for c in configuration:
        d = {}
        for item in c.split(','):
            value, color = item.split()
            d[color] = int(value)
        if any(color for color, value in d.items() if value > limit[color]):
            possible = False
            break
    if possible:
        s1 += int(game_id)
    # part 2
    mins = {'red': 0, 'green': 0, 'blue': 0}
    for cubes in configuration:
        for cube in cubes.split(','):
            i, cube = cube.split()
            mins[cube] = max(mins[cube], int(i))
    p = reduce(operator.mul, mins.values())
    s2 += p

print(s1)
print(s2)

