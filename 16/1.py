import sys

fields = {}

for line in sys.stdin:
    d = line.strip().split(":")
    if len(d) == 1:
        break
    ranges = list(map(tuple, [map(int, y.split("-")) for y in d[1].split("or")]))
    fields[d[0]] = ranges

for i in range(0,4):
    sys.stdin.readline()

tickets = [list(map(int, x.strip().split(","))) for x in sys.stdin]

def inRange(x, r):
    return (x >= r[0] and x <= r[1])

ans = 0
for ticket in tickets:
    for num in ticket:
        ok = False
        for r in fields.values():
            if inRange(num, r[0]) or inRange(num, r[1]):
                ok = True
        if not ok:
            ans += num
print(ans)

