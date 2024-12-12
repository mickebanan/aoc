import itertools
import pprint

import intcode

data = """3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"""
data = open('data/7.dat').read().strip()
p1 = p2 = 0
for phase in itertools.permutations('01234', 5):
    prev = 0
    for p in phase:
        machine = intcode.IntCode(data, inputs=[p, prev])
        value = machine.run()
        prev = value
    p1 = max(p1, prev)
print('part 1:', p1)

for phase in itertools.permutations('56789', 5):
    prev = 0
    machines = [intcode.IntCode(data, inputs=[phase[i]]) for i in range(5)]
    while any(not m.halted for m in machines):
        for m in machines:
            m.input(prev)
            value = m.run()
            if value is not None:
                prev = value
    p2 = max(p2, prev)
print('part 2:', p2)