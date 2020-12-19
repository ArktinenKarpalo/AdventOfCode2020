import sys
import itertools
import operator
import functools
import collections

rules = collections.defaultdict(list)

for line in sys.stdin:
    if len(line) == 1:
        break
    if line.find("\"") == -1:
        num = int(line[:line.find(":")])
        rule = list(map(lambda x: tuple(map(int, x.strip().split(" "))), line[line.find(":")+1:].split("|")))
        if num == 8:
            rule = [(42,), (42, 8)]
        elif num == 11:
            rule = [(42, 31)]
            rules[(11,31)].append(-1)
            rules[(42,-1,)].append(11)
        for p in rule:
            rules[p].append(num)
    else:
        num = int(line[:line.find(":")])
        rule = line[line.find(":")+3:-2]
        for p in rule:
            rules[p].append(num)
def ok(s: str):
    d = [[set() for y in range(len(s))] for x in range(len(s))]
    for i in range(len(s)):
        d[0][i].update(rules[s[i]])
        a = set()
        for r in d[0][i]:
            if (r,) in rules:
                a.update(rules[(r,)])
        d[0][i] |= a
    for j in range(1, len(s)):
        for i in range(len(s)-j):
            for k in range(1, j+1):
                for r1 in d[j-k][i]:
                    for r2 in d[k-1][i+j-k+1]:
                        if (r1, r2) in rules:
                            d[j][i].update(rules[(r1, r2)])
            a = set()
            for r in d[j][i]:
                if (r,) in rules:
                    a.update(rules[(r,)])
            d[j][i] |= a
    return (0 in d[len(s)-1][0])

ans = 0
for line in sys.stdin:
    if ok(line.strip()):
        ans += 1
print(ans)
