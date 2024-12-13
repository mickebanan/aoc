import re

import numpy as np

data = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".split('\n\n')
data = open('data/13.dat').read().split('\n\n')
machines = []
for m in data:
    a, b, prize = [m for m in m.split('\n') if m]
    ax, ay = re.match(r'Button A: X.(\d+), Y.(\d+)', a).groups()
    bx, by = re.match(r'Button B: X.(\d+), Y.(\d+)', b).groups()
    px, py = re.match(r'Prize: X=(\d+), Y=(\d+)', prize).groups()
    machines.append((np.array([[int(ax), int(bx)], [int(ay), int(by)]]),
                     np.array([int(px), int(py)])))

def solve(a, b):
    s = np.linalg.solve(a, b)
    # Kludgy way to only pick the integer solutions. It happens to work in this case.
    if np.all(np.abs(s - np.round(s)) < np.array([0.01, 0.01])):
        return 3*s[0] + s[1]
    return 0

p1 = p2 = 0
for a, b in machines:
    p1 += solve(a, b)
    b += np.array([10000000000000, 10000000000000])
    p2 += solve(a, b)
print('part 1:', int(p1))
print('part 2:', int(p2))
