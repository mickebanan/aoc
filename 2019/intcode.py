def parse(data):
    ip = 0
    while True:
        opcode = data[ip]
        length = 1
        if opcode == 99:
            break
        if opcode == 1:
            p1, p2, pv = data[ip + 1], data[ip + 2], data[ip + 3]
            v1, v2 = data[p1], data[p2]
            data[pv] = v1 + v2
            length = 4
        elif opcode == 2:
            p1, p2, pv = data[ip + 1], data[ip + 2], data[ip + 3]
            v1, v2 = data[p1], data[p2]
            data[pv] = v1 * v2
            length = 4
        ip += length
    return data