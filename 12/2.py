import sys
import math

input = [(lambda x: (x[0:1], int(x[1:len(x)])))(x.strip()) for x in sys.stdin]

s = [0, 0]
w = [10, 1]

for (i, d) in input:
    if i == 'N':
        w[1] += d
    elif i == 'S':
        w[1] -= d
    elif i == 'E':
        w[0] += d
    elif i == 'W':
        w[0] -= d
    elif i == 'R':
        rot = -d/180.0*math.pi
        w = [w[0]*math.cos(rot)-w[1]*math.sin(rot),
             w[0]*math.sin(rot)+w[1]*math.cos(rot)]
    elif i == 'L':
        rot = d/180.0*math.pi
        w = [w[0]*math.cos(rot)-w[1]*math.sin(rot),
             w[0]*math.sin(rot)+w[1]*math.cos(rot)]
    elif i == 'F':
        s[0] += w[0]*d
        s[1] += w[1]*d
print(int(round(math.fabs(s[0])+math.fabs(s[1]))))
