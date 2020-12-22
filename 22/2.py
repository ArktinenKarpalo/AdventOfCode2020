import sys
import copy
import collections as cl

p1 = cl.deque()
p2 = cl.deque()

input = "".join(list(sys.stdin))
input = input.split("\n\n")
for c in input[0][10:].split("\n"):
    p1.appendleft(int(c))
for c in input[1][10:-1].split("\n"):
    p2.appendleft(int(c))

def game(p1, p2):
    p1h = set() # May just work
    p2h = set()
    while len(p1) != 0 and len(p2) != 0:
        c1 = p1.pop()
        c2 = p2.pop()
        p1s = ",".join(map(str, p1))
        p2s = ",".join(map(str, p2))
        if p1s in p1h and p2s in p2h:
            return 1
        else:
            p1h.add(p1s)
            p2h.add(p2s)
        if c1 <= len(p1) and c2 <= len(p2): # Subgame
            p1s = copy.deepcopy(p1)
            p2s = copy.deepcopy(p2)
            for i in range(len(p1)-c1):
                p1s.popleft()
            for i in range(len(p2)-c2):
                p2s.popleft()
            if game(p1s, p2s) == 1:
                p1.extendleft([c1, c2])
            else:
                p2.extendleft([c2, c1])
        elif c1 > c2:
            p1.extendleft([c1, c2])
        else:
            p2.extendleft([c2, c1])
    if len(p1) == 0:
        return 2
    else:
        return 1

game(p1,p2)

ans = 0
for i in range(len(p1)):
    ans += (i+1)*p1[i]
for i in range(len(p2)):
    ans += (i+1)*p2[i]

print(ans)
