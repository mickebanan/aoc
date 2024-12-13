import re

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
    cx, cy = re.match(r'Prize: X=(\d+), Y=(\d+)', prize).groups()
    machines.append(((int(ax), int(ay)), (int(bx), int(by)), (int(cx), int(cy))))

def solve(x, y, p):
    # Solve using Cramer's rule.
    (ax, ay), (bx, by), (cx, cy) = x, y, p
    det = ax*by - bx*ay
    x = (cx*by - bx*cy) / det
    y = (ax*cy - cx*ay) / det
    if x == round(x) and y == round(y):
        return 3*x + y
    return 0

p1 = p2 = 0
for a, b, c in machines:
    p1 += solve(a, b, c)
    c = (c[0] + 10000000000000, c[1] + 10000000000000)
    p2 += solve(a, b, c)
print('part 1:', int(p1))
print('part 2:', int(p2))
