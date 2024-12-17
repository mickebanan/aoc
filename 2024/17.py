data = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
""".strip().split('\n\n')
data = open('data/17.dat').read().split('\n\n')
reg_a = int(data[0].split('\n')[0].split()[-1])
data = [int(a) for a in data[-1].split()[-1].split(',')]

def run(data, a):
    def get_combo_value(operand):
        return operand if operand < 4 else registers[operand]

    ip = 0
    s = []
    registers = {4: a, 5: 0, 6: 0}
    while ip < len(data):
        opcode = data[ip]
        operand = data[ip + 1]
        if opcode in (0, 6, 7):  # adv, bdv, cdv
            num = registers[4]
            den = 2 ** get_combo_value(operand)
            value = num // den
            if opcode == 0:
                registers[4] = value
            elif opcode == 6:
                registers[5] = value
            else:
                registers[6] = value
        elif opcode in (1, 4):  # bxl, bxc
            registers[5] ^= operand if opcode == 1 else registers[6]
        elif opcode == 2:  # bst
            registers[5] = get_combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if registers[4] != 0:
                ip = operand
                continue
        elif opcode == 5:  # out
            s.append(get_combo_value(operand) % 8)
        ip += 2
    return s

print('part 1:', ','.join(str(s) for s in run(data, reg_a)))

def p2():
    # Match ever longer substrings until the whole pattern is found.
    q = [[0]]
    test_len = 1
    while q:
        tests = q.pop(0)
        new_tests = []
        for test in tests:
            for step in range(8):
                # Resume searching from the last known partial match
                a = 8 * test + step
                x = run(data, a)
                if x == data:
                    yield a
                elif x == data[-test_len:]:
                    new_tests.append(a)
        if new_tests:
            q.append(new_tests)
            test_len += 1
print('part 2:', min(v for v in p2()))
