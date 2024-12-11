from functools import reduce
from operator import add, mul

data = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip().split('\n')
data = open('data/7.dat').read().strip().split('\n')

def concat(a, b):
    return int(str(a) + str(b))

def work(result, operands, operators):
    if len(operands) == 1:
        yield result == operands[0]
    else:
        for op in operators:
            v = reduce(op, operands[:2])
            yield from work(result, [v] + operands[2:], operators)

p1 = p2 = 0
for row in data:
    result, operands = row.split(': ')
    result = int(result)
    operands = [int(v) for v in operands.split(' ')]
    if any(a for a in work(result, operands, (add, mul))):
        p1 += result
    if any(a for a in work(result, operands, (add, mul, concat))):
        p2 += result
print('part 1:', p1)
print('part 2:', p2)