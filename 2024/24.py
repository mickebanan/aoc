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
orig_instructions = instructions[:]
xors = {}
ands = {}
ors = {}

def get_value(x, gates):
    return int(''.join(str(a[1]) for a in sorted(((k, v) for k, v in gates.items()
                                                  if k.startswith(x)), reverse=True)), 2)

def evaluate(gates, instructions, map_gates=False):
    gates = gates.copy()
    instructions = instructions[:]

    def get_next():
        for i, instruction in enumerate(instructions):
            op, to = instruction
            a, op, b = op.split(' ')
            if a in gates and b in gates:
                instructions.pop(i)
                return a, op, b, to

    def work():
        while instructions:
            a, op, b, to = get_next()
            if map_gates:
                pair = tuple(sorted((a, b)))
                match op:
                    case 'XOR':
                        if pair not in xors:
                            xors[pair] = to
                    case 'AND':
                        if pair not in ands:
                            ands[pair] = to
                    case 'OR':
                        if pair not in ors:
                            ors[pair] = to
            gates[to] = reduce(operators[op], (gates[a], gates[b]))
        return get_value('z', gates)
    return work()

def swap(instr, a, b):
    instr = instr[:]
    inputs, outputs = [a[0] for a in instr], [a[1] for a in instr]
    print('swapping %s with %s' % (a, b))
    v = outputs[outputs.index(b)]
    outputs[outputs.index(b)] = outputs[outputs.index(a)]
    outputs[outputs.index(a)] = v
    return list(zip(inputs, outputs))

print('part 1:', evaluate(gates, instructions))

# The gates were found by analyzing the output from the loop below and figuring
# out which ones to swap by checking the input data manually and calculating
# which gate should go where.
pairs = (('z06', 'jmq'), ('z13', 'gmh'), ('cbd', 'rqf'), ('z38', 'qrh'))
for a, b in pairs:
    instructions = swap(instructions, a, b)
evaluate(gates, instructions, map_gates=True)

print('part 2:', ','.join(sorted(a for pair in pairs for a in pair)))

# The circuit layout is the following, based on analyzing the input:
# x00/y00: half adder, outputs to z00 + nqp (carry bit)
# x01+/y01+/carry: full adder, outputs to z01+/carry etc. (carry bit carries forward to next circuit until z45)
# Inputs goes from 00-44.
# Diagrams from here: https://en.wikipedia.org/wiki/Adder_(electronics)
carry = None
for digit in range(45):  # according to input
    digit = ('00' + str(digit))[-2:]
    x, y = 'x' + digit, 'y' + digit
    if digit == '00':
        print('DIGIT:', digit)
        # half adder
        if (x, y) in xors:
            if 'z00' != xors.pop((x, y)):
                print('OUTPUT ERROR: z00')
        if (x, y) in ands:
            carry = ands.pop((x, y))
    else:
        print('DIGIT:', digit)
        print('carry:', carry)
        # full adder
        xor1_output = None
        and1_output = None
        mid = None
        if (x, y) in xors:
            print((x, y), 'in xors 1')
            xor1_output = xors.pop((x, y))
            print('xor 1:', xor1_output)
        else:
            print('missing?!', x, y)
        if (x, y) in ands:
            print((x, y), 'in ands 2')
            and1_output = ands.pop((x, y))
            print('and 1:', and1_output)
        else:
            print('missing and?!', x, y)
        t = tuple(sorted((xor1_output, carry)))
        if t in xors:
            print(t, 'in xors 3')
            o = xors.pop(t)
            print('output:', o)
            if 'z' + digit != o:
                print('OUTPUT ERROR: z' + digit, o)
        else:
            print('missing xor 3?!', t)
        if t in ands:
            print(t, 'in ands 4')
            mid = ands.pop(t)
            print('mid:', mid)
        else:
            print('missing and 4?!', t)
        try:
            t = tuple(sorted((mid, and1_output)))
        except TypeError:
            print('BOOOO!!!')
            continue
        if t in ors:
            carry = ors.pop(t)
            print(t, 'in ors 5, set carry to', carry)
        else:
            print('missing or?!', t)