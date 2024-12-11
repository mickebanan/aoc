data = '16,1,2,0,4,2,7,1,2,14'
with open('7.dat') as f:
    data = f.readline()

data = [int(a) for a in data.split(',')]

# part 1
min_fuel = None
for pos in range(len(data) + 1):
    fuel = 0
    for crab in data:
        fuel += abs(crab - pos)
        if min_fuel and fuel > min_fuel:
            break
    if not min_fuel:
        min_fuel = fuel
    min_fuel = min(fuel, min_fuel)
print('part 1:', min_fuel)

# part 2
min_fuel = None
for pos in range(len(data) + 1):
    fuel = 0
    for crab in data:
        fuel += sum(range(abs(crab - pos) + 1))
        if min_fuel and fuel > min_fuel:
            break
    if not min_fuel:
        min_fuel = fuel
    min_fuel = min(fuel, min_fuel)
print('part 2:', min_fuel)
