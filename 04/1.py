import sys
import itertools

def valid(fields):
    for x in current:
        if x.startswith("cid:"):
            return len(fields) == 8
    return len(fields) == 7
ans = 0

current = []
for line in sys.stdin:
    if line == "\n":
        ans += valid(current)
        current = []
    else:
        current.extend(line.split())
ans += valid(current)
print(ans)
