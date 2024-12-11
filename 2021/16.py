import operator
from functools import reduce

data = [
    # 'D2FE28',
    # '38006F45291200',
    # 'EE00D40C823060',
    # '8A004A801A8002F478',
    # '620080001611562C8802118E34',
    # 'C0015000016115A2E0802F182340',
    # 'A0016C880162017C3686B18A3D4780',
    # 'C200B40A82',
    # '04005AC33890',
    '9C0141080250320F1802104A08',
]
with open('16.dat') as f:
    data = [row.strip() for row in f.readlines()]
hex_to_bits = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}
for i, row in enumerate(data):
    data[i] = ''.join(hex_to_bits[c] for c in row)

ops = {
    0: operator.add,
    1: operator.mul,
    2: min,
    3: max,
    5: operator.gt,
    6: operator.lt,
    7: operator.eq,
}


def parse(line):
    pos = 0
    version = 0

    def read(n):
        nonlocal pos
        val = line[pos:pos + n]
        pos += n
        return int(val, 2)

    def parse_packet():
        nonlocal version, pos
        ver = read(3)
        version += ver
        ptype = read(3)
        if ptype == 4:  # literal
            cont, val = read(1), read(4)
            while cont:
                cont = read(1)
                val = val << 4 | read(4)
            return val
        else:  # operator
            ltype = read(1)
            if ltype:  # subpacket amount
                amount = read(11)
                values = []
                for _ in range(amount):
                    values.append(parse_packet())
                return reduce(ops[ptype], values)
            else:  # subpacket length
                length = read(15) + pos
                values = []
                while pos < length:
                    values.append(parse_packet())
                return reduce(ops[ptype], values)

    tot = parse_packet()
    return version, tot


a, tot = parse(data[0])
print('part 1:', a)
print('part 2:', tot)
