import collections
import itertools

data = [  # part 1 test
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
]
data = [  # part 2 test
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]
with open('input/1.dat') as f:
    data = [line.strip() for line in f.readlines()]

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
reversed_numbers = {''.join(reversed(n)): a for n, a in numbers.items()}


def check(input, nums=None):
    for i, _ in enumerate(input):
        if input[i].isnumeric():
            return input[i]
        if nums:
            for number in nums:
                if input[i:].startswith(number):
                    return nums[number]


# part 1
s = []
for line in data:
    row = [check(line), check(''.join(reversed(line)))]
    s.append(''.join(row))
print(sum(int(a) for a in s))

# part 2
s = []
for line in data:
    row = [check(line, nums=numbers), check(''.join(reversed(line)), nums=reversed_numbers)]
    s.append(''.join(row))
print(sum(int(a) for a in s))
