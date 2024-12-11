if __name__ == '__main__':
    d = {}
    with open('1.input') as f:
        elf = 0
        s = 0
        for row in f:
            try:
                value = int(row)
            except ValueError:
                d[elf] = s
                elf += 1
                s = 0
            else:
                s += value
    m = (0, 0)
    for k, v in d.items():
        if v >= m[1]:
            m = (k, v)
            print('new max', m)
    d.pop(m[0])
    m = (0, 0)
    for k, v in d.items():
        if v >= m[1]:
            m = (k, v)
            print('new max', m)
    d.pop(m[0])
    m = (0, 0)
    for k, v in d.items():
        if v >= m[1]:
            m = (k, v)
            print('new max', m)
