import intcode

data = "2,4,4,5,99,0"
data = open('data/2.dat').read()
data = [int(a) for a in data.split(',')]

data_p1 = data[:]
data_p1[1] = 12
data_p1[2] = 2
machine = intcode.IntCode(data_p1)
machine.run()
print('part 1:', machine.get(0))

def p2():
    for verb in range(100):
        for noun in range(100):
            data_p2 = data[:]
            data_p2[1] = verb
            data_p2[2] = noun
            machine = intcode.IntCode(data_p2)
            machine.run()
            if machine.get(0) == 19690720:
                return 100 * verb + noun
print('part 2:', p2())