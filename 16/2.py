import sys
import functools

fields = {}

for line in sys.stdin:
    d = line.strip().split(":")
    if len(d) == 1:
        break
    ranges = list(map(tuple, [map(int, y.split("-")) for y in d[1].split("or")]))
    fields[d[0]] = ranges

sys.stdin.readline()
our = list(map(int, sys.stdin.readline().strip().split(",")))
for i in range(0,2):
    sys.stdin.readline()

tickets = [list(map(int, x.strip().split(","))) for x in sys.stdin]

def in_range(x, r):
    return (x >= r[0] and x <= r[1])

def valid_fields(num):
    for (k,r) in fields.items():
        if in_range(num, r[0]) or in_range(num, r[1]):
            yield k

def invalid(ticket):
    for num in ticket:
        if len(list(valid_fields(num))) == 0:
            return False
    return True
tickets = list(filter(invalid, tickets))

lol = []
for i in range(0, len(fields)):
    lol.append((functools.reduce(lambda x, y: x & set(valid_fields(y[i])), tickets, set(fields.keys())), i))
lol.sort(key=lambda x: len(x[0]))
a = set()
ans = 1
for s in lol:
    col = next(iter((s[0]-a)))
    if col.startswith("departure"):
        ans *= our[s[1]]
    a |= s[0]
print(ans)
