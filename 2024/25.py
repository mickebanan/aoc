data = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
""".strip().split('\n\n')
data = open('data/25.dat').read().strip().split('\n\n')
locks = []
keys = []
for line in data:
    rows = line.splitlines()
    cols = [0] * len(rows[0])
    if '#' in rows[0]:
        for row in rows[1:]:
            for i, c in enumerate(row):
                if c == '#':
                    cols[i] += 1
        locks.append(cols)
    else:
        for row in rows[:-1]:
            for i, c in enumerate(row):
                if c == '#':
                    cols[i] += 1
        keys.append(cols)

p1 = 0
for lock in locks:
    for key in keys:
        if all(sum(a) <= 5 for a in zip(lock, key)):
            p1 += 1
print('part 1:', p1)

