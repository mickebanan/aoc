import math
import operator
import pprint

data = [
    'Monkey 0:',
      'Starting items: 79, 98',
      'Operation: lambda v: v * 19',
      # 'Operation: new = old * 19',
      'Test: divisible by 23',
        'If true: throw to monkey 2',
        'If false: throw to monkey 3',
    'Monkey 1:',
      'Starting items: 54, 65, 75, 74',
      'Operation: lambda v: v + 6',
      # 'Operation: new = old + 6',
      'Test: divisible by 19',
        'If true: throw to monkey 2',
        'If false: throw to monkey 0',
    'Monkey 2:',
      'Starting items: 79, 60, 97',
      'Operation: lambda v: v * v',
      # 'Operation: new = old * old',
      'Test: divisible by 13',
        'If true: throw to monkey 1',
        'If false: throw to monkey 3',
    'Monkey 3:',
      'Starting items: 74',
      'Operation: lambda v: v + 3',
      # 'Operation: new = old + 3',
      'Test: divisible by 17',
        'If true: throw to monkey 0',
        'If false: throw to monkey 1',
]
data = [
    'Monkey 0:',
    'Starting items: 73, 77',
    # 'Operation: new = old * 5',
    'Operation: lambda v: v * 5',
    'Test: divisible by 11',
    'If true: throw to monkey 6',
    'If false: throw to monkey 5',
    'Monkey 1:',
    'Starting items: 57, 88, 80',
    # 'Operation: new = old + 5',
    'Operation: lambda v: v + 5',
    'Test: divisible by 19',
    'If true: throw to monkey 6',
    'If false: throw to monkey 0',
    'Monkey 2:',
    'Starting items: 61, 81, 84, 69, 77, 88',
    # 'Operation: new = old * 19',
    'Operation: lambda v: v * 19',
    'Test: divisible by 5',
    'If true: throw to monkey 3',
    'If false: throw to monkey 1',
    'Monkey 3:',
    'Starting items: 78, 89, 71, 60, 81, 84, 87, 75',
    # 'Operation: new = old + 7',
    'Operation: lambda v: v + 7',
    'Test: divisible by 3',
    'If true: throw to monkey 1',
    'If false: throw to monkey 0',
    'Monkey 4:',
    'Starting items: 60, 76, 90, 63, 86, 87, 89',
    # 'Operation: new = old + 2',
    'Operation: lambda v: v + 2',
    'Test: divisible by 13',
    'If true: throw to monkey 2',
    'If false: throw to monkey 7',
    'Monkey 5:',
    'Starting items: 88',
    # 'Operation: new = old + 1',
    'Operation: lambda v: v + 1',
    'Test: divisible by 17',
    'If true: throw to monkey 4',
    'If false: throw to monkey 7',
    'Monkey 6:',
    'Starting items: 84, 98, 78, 85',
    # 'Operation: new = old * old',
    'Operation: lambda v: v * v',
    'Test: divisible by 7',
    'If true: throw to monkey 5',
    'If false: throw to monkey 4',
    'Monkey 7:',
    'Starting items: 98, 89, 78, 73, 71',
    # 'Operation: new = old + 4',
    'Operation: lambda v: v + 4',
    'Test: divisible by 2',
    'If true: throw to monkey 3',
    'If false: throw to monkey 2',
]
monkeys = {}
monkey = None
for row in data:
    if row.startswith('Monkey'):
        if monkey:
            name = len(monkeys)
            monkeys[name] = monkey
        monkey = {'test': {}, 'inspections': 0}
    else:
        text, value = row.split(':', 1)
        if text == 'Starting items':
            monkey['items'] = [int(v) for v in value.split(',')]
        elif text == 'Operation':
            monkey[text.lower()] = eval(value)
        elif text == 'Test':
            value = value.split()
            monkey['test']['divisor'] = int(value[-1])
        elif text == 'If true':
            monkey['test']['true'] = int(value.split()[-1])
        elif text == 'If false':
            monkey['test']['false'] = int(value.split()[-1])
if monkey:
    name = len(monkeys)
    monkeys[name] = monkey
divisors = [d['test']['divisor'] for d in monkeys.values()]
max_worry = math.lcm(*divisors)
print('divisor:', max_worry)

for _ in range(10000):
    for monkey, d in monkeys.items():
        items = d['items'][:]
        d['items'] = []
        for item in items:
            d['inspections'] += 1
            worry_level = d['operation'](item)
            # worry_level //= 3
            worry_level %= max_worry
            if worry_level % d['test']['divisor'] == 0:
                monkeys[d['test']['true']]['items'].append(worry_level)
            else:
                monkeys[d['test']['false']]['items'].append(worry_level)
# pprint.pprint(monkeys)
print('inspection product:')
print(operator.mul(*[v['inspections'] for v in sorted(monkeys.values(), key=lambda v: v['inspections'], reverse=True)[:2]]))
