import itertools

data = [
    '0 3 6 9 12 15',
    '1 3 6 10 15 21',
    '10 13 16 21 30 45',
]
with open('input/9.dat') as f:
    data = [row.strip() for row in f.readlines()]
_data = {}
for i, row in enumerate(data):
    _data[i] = [[int(a) for a in row.split()]]
data = _data

for row, values in data.items():
    value = values[0]
    while True:
        next_row = []
        for v1, v2 in itertools.pairwise(value):
            next_row.append(v2 - v1)
        data[row].append(next_row)
        value = next_row
        if sum(next_row) == 0:
            break
    for i, value in enumerate(reversed(values)):
        if i == 0:
            value.append(0)
            value.insert(0, 0)
        else:
            v = value[-1] + values[len(values) - i][-1]
            value.append(v)
            v = value[0] - values[len(values) - i][0]
            value.insert(0, v)


print('part 1:', sum(v[0][-1] for v in data.values()))
print('part 2:', sum(v[0][0] for v in data.values()))
