data = """
12
14
1969
100756""".strip().split('\n')
data = open('data/1.dat').read().strip().split('\n')
p1 = p2 = 0
for value in data:
    value = int(value) // 3 - 2
    p1 += value
    while value > 0:
        p2 += value
        value = value // 3 - 2
print('part 1:', p1)
print('part 2:', p2)