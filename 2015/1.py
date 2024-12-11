data = open('data/1.dat').read().strip()
p1 = p2 = 0

for i, c in enumerate(data, start=1):
    p1 += 1 if c == '(' else -1
    if p1 < 0 and not p2:
        p2 = i
print('p1:', p1)
print('p2:', p2)