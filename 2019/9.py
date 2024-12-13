import intcode

data = "109, 1, 203, 2, 204, 2, 99"
data = open('data/9.dat').read().strip()

a = intcode.IntCode(data, inputs=[1])
while not a.halted:
    v = a.run()
    if v:
        print('part 1:', v)
a = intcode.IntCode(data, inputs=[2])
while not a.halted:
    v = a.run()
    if v:
        print('part 2:', v)