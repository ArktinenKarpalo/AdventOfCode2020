import sys
import itertools
import operator
import functools
import collections

rules = {}

e = collections.defaultdict(list)

s_r = set()
r_s = collections.defaultdict(list)

s = []

for line in sys.stdin:
    if len(line) == 1:
        break
    if line.find("\"") == -1:
        num = int(line[:line.find(":")])
        rule = list(map(lambda x: tuple(map(int, x.strip().split(" "))), line[line.find(":")+1:].split("|")))
        for p in rule:
            for n in p:
                e[n].append(num)
        rules[num] = rule
    else:
        num = int(line[:line.find(":")])
        rule = line[line.find(":")+3:-2]
        r_s[num].append(rule)
        s_r.add(rule)
        rules[num] = rule
        s.append(num)

ord = []
vis = set()
def dfs(cur):
    if cur in vis:
        return
    vis.add(cur)
    for n in e[cur]:
        dfs(n)
    ord.append(cur)
for n in s:
    dfs(n)
ord.reverse()

for n in ord:
    if type(rules[n]) is list:
        res = []
        for rule in rules[n]:
            res += list(map(lambda x: functools.reduce(operator.add, x),itertools.product(*list(map(lambda x: r_s[x], rule)))))
        r_s[n] += res
        for s in res:
            s_r.add(s)

input = list(map(lambda x: x.strip(), sys.stdin))
ans = 0
for line in input:
    if line in s_r:
        ans += 1
print(ans)
