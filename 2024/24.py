from functools import reduce
from operator import and_, or_, xor

data = open('data/24.dat').read().strip().split('\n\n')
gates = {}
instructions = []
for row in data[0].splitlines():
    gate, value = row.split(': ')
    gates[gate] = int(value)
for row in data[1].splitlines():
    instructions.append(tuple(row.split(' -> ')))
operators = {'AND': and_, 'OR': or_, 'XOR': xor}

def get_next(instructions):
    for i, instruction in enumerate(instructions):
        op, to = instruction
        a, op, b = op.split(' ')
        if a in gates and b in gates:
            instructions.pop(i)
            return a, op, b, to

def get_value(x, gates):
    return int(''.join(str(a[1]) for a in sorted(((k, v) for k, v in gates.items()
                                                  if k.startswith(x)), reverse=True)), 2)

def work(instructions, gates):
    while instructions:
        a, op, b, to = get_next(instructions)
        gates[to] = reduce(operators[op], (gates[a], gates[b]))
    return get_value('z', gates)
print('part 1:', work(instructions[:], gates))

