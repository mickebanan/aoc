data = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
]
# data = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
with open('8.dat') as f:
    data = [row.strip() for row in f.readlines()]

# part 1
s = 0
for row in data:
    _, output = row.split('|')
    output = output.split()
    s += sum(1 for p in output if len(p) in (2, 3, 4, 7))
print('part 1:', s)

# part 2
total = 0
for row in data:
    # Hideous way to figure out what string corresponds to which number
    # based on overlapping fields.
    pattern, output = row.split('|')
    pattern = pattern.split()
    output = output.split()
    matches = {}
    numbers = pattern + output
    for n in numbers[:]:
        if len(n) == 2:
            matches['1'] = set(n)
            numbers.remove(n)
        elif len(n) == 3:
            matches['7'] = set(n)
            numbers.remove(n)
        elif len(n) == 4:
            matches['4'] = set(n)
            numbers.remove(n)
        elif len(n) == 7:
            matches['8'] = set(n)
            numbers.remove(n)
    for n in numbers[:]:
        if len(set(n) - matches['7']) == 2:
            matches['3'] = set(n)
            numbers.remove(n)
        elif len(set(n) - matches['7']) == 4:
            matches['6'] = set(n)
            numbers.remove(n)
    for n in numbers[:]:
        if len(set(n) - matches['6']) == 0:
            matches['5'] = set(n)
            numbers.remove(n)
    for n in numbers[:]:
        if len(n) == 6 and len(set(n) - matches['5'] - matches['1']) == 0:
            matches['9'] = set(n)
            numbers.remove(n)
    for n in numbers:
        if len(n) == 5:
            matches['2'] = set(n)
        elif len(n) == 6:
            matches['0'] = set(n)
    s = ''
    for o in output:
        so = set(o)
        for n, v in matches.items():
            # Check for matching sets to determine what string corresponds to
            # which number.
            if so <= v <= so:
                s += n
                break
    total += int(s)
print('part 2:', total)
