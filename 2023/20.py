import math

data = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""
data = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""
data = open('input/20.dat').read().strip()
flipflops = {}
conjunctions = {}
targets = {}
rx_source = None
rx_values = {}
for row in data.strip().split('\n'):
    source, destination = row.split(' -> ')
    destination = destination.split(', ')
    if 'rx' in destination:
        rx_source = source[1:]
    if source[0] in '&%':
        targets[source[1:]] = destination
        if source[0] == '%':
            flipflops[source[1:]] = 0
        else:
            conjunctions[source[1:]] = {}
    else:
        targets[source] = destination
for c in conjunctions.copy():
    for n, t in targets.items():
        if c in t:
            conjunctions[c][n] = 0
            if c == rx_source:
                rx_values[n] = 0

sums = [0, 0]
i = 0
while True:
    if all(rx_values.values()):
        break
    q = [('broadcaster', 0)]
    if i < 1000:
        sums[0] += 1  # pressing button
    while q:
        node, value = q.pop(0)
        value = int(value)
        if node not in targets:
            continue
        if node in rx_values and value and not rx_values[node]:
            rx_values[node] = i + 1  # add one due to an additional button press needed to yield the signal
        for t in targets[node]:
            if i < 1000:
                sums[value] += 1
            if t in flipflops and not value:
                flipflops[t] = int(not flipflops[t])
                q.append((t, flipflops[t]))
            elif t in conjunctions:
                conjunctions[t][node] = value
                q.append((t, not all(conjunctions[t].values())))
    i += 1

print('part 1:', math.prod(sums))
print('part 2:', math.prod(rx_values.values()))
