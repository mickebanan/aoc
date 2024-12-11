import helpers

data = """
3   4
4   3
2   5
1   3
3   9
3   3""".split('\n')
data = open('data/1.dat').readlines()
values = [tuple(row.split()) for row in data if row]
first = sorted(int(t[0]) for t in values)
second1 = sorted(int(t[1]) for t in values)
second2 = second1.copy()

@helpers.timer
def solve():
    p1 = p2 = 0
    for v1 in first:
        v2 = second1.pop(0)
        p1 += abs(v1 - v2)
        score = len([v2 for v2 in second2 if v2 == v1])
        p2 += v1 * score
    print('part 1:', p1)
    print('part 2:', p2)
solve()