import intcode

data = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""
data = open('data/5.dat').read().strip()
data = [int(a) for a in data.split(',')]
# print(data)
intcode.parse(data)