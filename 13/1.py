import sys
import math
earliest = int(sys.stdin.readline())
timetable = [int(x) for x in filter(lambda x: x != 'x', sys.stdin.readline().split(","))]
ans = (math.inf, 0)
for id in timetable:
    w = id-earliest%id
    if earliest%id == 0:
        ans = (0, id)
    elif w < ans[0]:
        ans = (w, id)
print(ans[0]*ans[1])
