import sys
import math
earliest = int(sys.stdin.readline())
timetable = [x for x in sys.stdin.readline().strip().split(",")]

l = []
for i in range(0, len(timetable)):
    if timetable[i] == 'x':
        continue;
    l.append((int(timetable[i]), i))
inc = l[0][0]
cur = inc
mon = 1
while mon != len(l):
    cur += inc
    for i in range(mon, len(l)):
        if (cur+l[i][1])%l[i][0] != 0:
            break
        else:
            mon += 1
            inc *= l[i][0]
print(cur)
