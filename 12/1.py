import sys
import math

input = [(lambda x: (x[0:1], int(x[1:len(x)])))(x.strip()) for x in sys.stdin]

rot = 0
x = 0
y = 0

for ins in input:
    if ins[0] == 'N':
        y += ins[1]
    elif ins[0] == 'S':
        y -= ins[1]
    elif ins[0] == 'E':
        x += ins[1]
    elif ins[0] == 'W':
        x -= ins[1]
    elif ins[0] == 'R':
        rot -= ins[1]/180.0*math.pi
    elif ins[0] == 'L':
        rot += ins[1]/180.0*math.pi
    else: # F
        x += math.cos(rot)*ins[1]
        y += math.sin(rot)*ins[1]
print(int(round(math.fabs(x)+math.fabs(y))))
