import collections
import operator
from functools import reduce

data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
data = open('input/15.dat').read()

p1 = p2 = 0
m = collections.defaultdict(list)

for value in (d for d in data.split(',')):
    v = 0
    key = op = None
    for c in value:
        if c in ('-', '='):
            key = v
            op = c
        v = (v + ord(c)) * 17 % 256
    p1 += v
    value = value.split(op)
    for j, (a, b) in enumerate(m[key]):
        if a == value[0]:
            if op == '-':
                m[key].pop(j)
            else:
                m[key][j] = value
            break
    else:
        if op == '=':
            m[key].append(value)

for k, v in m.items():
    if v:
        p2 += (1 + k) * reduce(operator.add, (i * int(b) for i, (a, b) in enumerate(v, start=1)))

print('part 1:', p1)
print('part 2:', p2)
