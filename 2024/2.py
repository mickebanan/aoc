import itertools

import helpers

data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".strip().split('\n')
data = open('data/2.dat').readlines()

def check_values(values):
    first = values[0]
    potential_errors = set()
    for i, (v1, v2) in enumerate(itertools.pairwise(values)):
        if v1 < v2 and 1 <= (v2 - v1) <= 3 and first < v2:
            pass
        elif v1 > v2 and 1 <= (v1 - v2) <= 3 and first > v2:
            pass
        else:
            potential_errors |= {i - 1, i, i + 1}
    if potential_errors:
        return potential_errors
    if values == sorted(values) or values == sorted(values, reverse=True):
        return True
    return False

@helpers.timer
def solve():
    p1 = p2 = 0
    for row in data:
        values = [int(v) for v in row.split()]
        ret = check_values(values)
        if ret is True:
            p1 += 1
        else:
            for v in sorted(ret):
                vals = values[:v] + values[v+1:]
                if check_values(vals) is True:
                    p2 += 1
                    break
    print('part 1:', p1)
    print('part 2:', p1 + p2)
solve()