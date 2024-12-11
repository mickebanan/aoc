import operator
from functools import reduce

import helpers

data = [
    'Time:      7  15   30',
    'Distance:  9  40  200',
]
data = [
    'Time:        41     77     70     96',
    'Distance:   249   1362   1127   1011',
]

times = data[0].split()[1:]
distances = data[1].split()[1:]


def search(time, distance):
    # Binary search from the left
    lower, upper = 0, time
    while lower < upper:
        mid = (lower + upper) // 2
        value = (time - mid) * mid
        if value <= distance:
            lower = mid + 1
        else:
            upper = mid
    return lower


def get_wins(time, distance):
    # The computed distances describe a bell curve, so it's enough to just find the winning start and end points.
    # Everything in between is automatically going to win too.
    # The curve is symmetric so finding the start point is enough to determine the end point.
    start = search(time, distance)
    end = time - start + 1
    return end - start


@helpers.timer
def p1():
    wins = []
    for time, distance in zip(times, distances):
        wins.append(get_wins(int(time), int(distance)))
    print('part 1:', reduce(operator.mul, wins))


@helpers.timer
def p2():
    time, distance = int(''.join(times)), int(''.join(distances))
    print('part 2:', get_wins(time, distance))


p1()
p2()
