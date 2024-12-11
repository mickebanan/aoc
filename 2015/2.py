data = """
2x3x4
1x1x10
""".strip().split('\n')
data = open('data/2.dat').read().strip().split('\n')

p1 = p2 = 0
for row in data:
    l, w, h = row.split('x')
    l, w, h = int(l), int(w), int(h)
    area = 2*l*h + 2*w*h + 2*l*w
    slack = min(l*h, w*h, l*w)
    p1 += area + slack
    sides = sorted([l, w, h])
    ribbon = 2*sides[0] + 2*sides[1] + l*w*h
    p2 += ribbon
print('p1', p1)
print('p2', p2)