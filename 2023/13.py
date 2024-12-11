from helpers import transpose

data = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


def diff(a, b):
    return sum(x != y for x, y in zip(a, b))


def check(pattern, fixes=0):
    orig_reflection = -1
    if fixes:
        orig_reflection = check(pattern)
    for i in range(1, len(pattern)):
        errors = 0
        for bw, fw in zip(reversed(pattern[:i]), pattern[i:]):
            errors += diff(bw, fw)
            if errors > fixes:
                break
        else:
            if i != orig_reflection:
                return i
    return 0


pattern = []
p1 = p2 = 0
data = open('input/13.dat').read()
for row in data.split('\n'):
    if row:
        pattern.append(row)
    elif pattern:
        p1 += 100 * check(pattern) or check(transpose(pattern))
        p2 += 100 * check(pattern, fixes=1) or check(transpose(pattern), fixes=1)
        pattern = []
print('part 1:', p1)
print('part 2:', p2)
