import sys
import itertools

input = "".join([s for s in sys.stdin])
input = input.split("\n\n")

ans = 0
for x in input:
    s = set()
    for c in itertools.chain.from_iterable(x.split("\n")):
        s.add(c)
    ans += len(s)

print(ans)
