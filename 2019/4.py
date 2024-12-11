import collections
import itertools

data = "265275-781584"
start, stop = data.split("-")
p1 = p2 = 0
for value in range(int(start), int(stop) + 1):
    counts = collections.Counter(str(value))
    adjacent = False
    increasing = True
    two_count = False
    for a, b in itertools.pairwise(str(value)):
        if a == b:
            adjacent = True
            if counts[a] == 2:
                two_count = True
        if b < a:
            increasing = False
            break
    if adjacent and increasing:
        p1 += 1
        if two_count:
            p2 += 1
print('part 1:', p1)
print('part 2:', p2)