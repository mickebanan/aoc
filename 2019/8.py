import collections
import itertools

data = open('data/8.dat').read().strip()
width = 25
height = 6
layers = []
i = 0
while i < len(data):
    layer = []
    for _ in range(width * height):
        layer.append(int(data[i]))
        i += 1
    layers.append(layer)
min_value = 1_000_000
fewest = 0
for i, layer in enumerate(layers):
    c = collections.Counter(layer)
    if c[0] < min_value:
        min_value = c[0]
        fewest = i
c = collections.Counter(layers[fewest])
print('part 1:', c[1] * c[2])

image = [0] * width * height
for i in range(width * height):
    for layer in layers:
        if layer[i] == 2:
            continue
        image[i] = layer[i]
        break
print('part 2:')
for row in itertools.batched(image, width):
    print(''.join(str('#' if a else ' ') for a in row))