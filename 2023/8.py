import itertools
import math
import re

import helpers

data = [
    'RL',
    '',
    'AAA = (BBB, CCC)',
    'BBB = (DDD, EEE)',
    'CCC = (ZZZ, GGG)',
    'DDD = (DDD, DDD)',
    'EEE = (EEE, EEE)',
    'GGG = (GGG, GGG)',
    'ZZZ = (ZZZ, ZZZ)',
]
data = [
    'LLR',
    '',
    'AAA = (BBB, BBB)',
    'BBB = (AAA, ZZZ)',
    'ZZZ = (ZZZ, ZZZ)',
]
data = [
    'LR',
    '',
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)',
]
with open('input/8.dat') as f:
    data = [row.strip() for row in f.readlines()]
instructions = data[0]
moves = {}
for row in data[2:]:
    m = re.match(r'(\w+) = \((\w+), (\w+)\)', row)
    moves[m[1]] = (m[2], m[3])


def work(where, instructions):
    steps = 0
    lr = {'L': 0, 'R': 1}
    while not where.endswith('Z'):
        steps += 1
        where = moves[where][lr[next(instructions)]]
    return steps


def p1():
    start = 'AAA'
    steps = work(start, itertools.cycle(instructions))
    print('part 1:', steps)


@helpers.timer
def p2():
    locations = [k for k in moves if k.endswith('A')]
    instrs = itertools.cycle(instructions)
    ends = [work(loc, instrs) for loc in locations]
    print('part 2:', math.lcm(*ends))


p1()
p2()
