import helpers

data = """target area: x=20..30, y=-10..-5"""
data = """target area: x=94..151, y=-156..-103"""
data = data.split(':')[1].strip()
xs, ys = data.split(', ')
xs, ys = xs.split('..'), ys.split('..')
xs = (int(xs[0][len('x='):]), int(xs[1]))
ys = (int(ys[0][len('y='):]), int(ys[1]))
xmax = max(xs)
xmin = min(xs)
ymax = max(ys)
ymin = min(ys)


class Shell:
    x_vel = None
    y_vel = None
    x = None
    y = None

    def __init__(self, x, y):
        self.x_vel = x
        self.y_vel = y
        self.x = 0
        self.y = 0

    def __str__(self):
        return '(%s, %s) (xv: %s, yv: %s)' % (self.x, self.y, self.x_vel, self.y_vel)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.y_vel -= 1
        if self.x_vel > 0:
            self.x_vel -= 1
        elif self.x_vel < 0:
            self.x_vel += 1

    def on_target(self):
        if ys[0] <= self.y <= ys[1] and xs[0] <= self.x <= xs[1]:
            return True
        return False

    def overshot(self):
        if self.x > xmax or self.y < ymin:
            return True
        return False

    def shoot(self):
        highest = []
        while True:
            self.move()
            highest.append(self.y)
            if self.on_target():
                return max(highest)
            if self.overshot():
                return None


@helpers.timer
def launch():
    best = []
    hits = set()
    for x in range(xmax + 1):
        for y in range(ymin, abs(ymax) * 2):
            shell = Shell(x, y)
            a = shell.shoot()
            if a is not None:
                hits.add((x, y))
                best.append(a)
    print('part 1:', max(best))
    print('part 2:', len(hits))


launch()

