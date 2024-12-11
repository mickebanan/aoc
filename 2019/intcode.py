def parse(data):
    c = 0
    ip = 0
    while True:
        c += 1
        if c > 1000:
            break
        opcode = data[ip]
        length = 0
        opcode = ('00000' + str(opcode))[-5:]
        parameters, opcode = opcode[:3], opcode[3:]
        opcode = int(opcode)
        if opcode == 99:  # Return
            break
        if opcode in (1, 2, 7, 8):  # +/*/</==
            p1, p2, pv = data[ip + 1], data[ip + 2], data[ip + 3]
            v1 = data[p1] if parameters[-1] == '0' else p1
            v2 = data[p2] if parameters[-2] == '0' else p2
            if opcode == 1:
                data[pv] = v1 + v2
            elif opcode == 2:
                data[pv] = v1 * v2
            elif opcode == 7:
                data[pv] = 1 if v1 < v2 else 0
            elif opcode == 8:
                data[pv] = 1 if v1 == v2 else 0
            length = 4
        elif opcode == 3:  # Input
            pv = data[ip + 1]
            value = input(' > ')
            data[pv] = int(value)
            length = 2
        elif opcode == 4:  # Output
            if parameters[-1] == '0':
                pv = data[data[ip + 1]]
            else:
                pv = data[ip + 1]
            print(pv)
            length = 2
        elif opcode in (5, 6):  # Jump if true/false
            p1, p2 = data[ip + 1], data[ip + 2]
            v1 = data[p1] if parameters[-1] == '0' else p1
            v2 = data[p2] if parameters[-2] == '0' else p2
            if opcode == 5 and v1 != 0:
                ip = v2
                continue
            elif opcode == 6 and v1 == 0:
                ip = v2
                continue
            length = 3
        ip += length
    return data