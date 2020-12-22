import sys
import collections as cl

p1 = cl.deque()
p2 = cl.deque()

input = "".join(list(sys.stdin))
input = input.split("\n\n")
for c in input[0][10:].split("\n"):
    p1.appendleft(int(c))
for c in input[1][10:-1].split("\n"):
    p2.appendleft(int(c))

while len(p1) != 0 and len(p2) != 0:
    c1 = p1.pop()
    c2 = p2.pop()
    if c1 > c2:
        p1.extendleft([c1, c2])
    else:
        p2.extendleft([c2, c1])

ans = 0
for i in range(len(p1)):
    ans += (i+1)*p1[i]
for i in range(len(p2)):
    ans += (i+1)*p2[i]

print(ans)
