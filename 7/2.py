import sys
import collections
import re
import queue

mp = collections.defaultdict(list)
bg = collections.defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    color = re.match("(.*?) bags?", line).group(1)
    for num, c in re.findall("([0-9]+) ([^,.]+) bags?", line):
         mp[color].append((c, int(num)))

t = []
vis = set()
def haku(s):
    if s in vis:
        return
    vis.add(s)
    for c in mp[s]:
        haku(c[0])
    t.append(s)
haku("shiny gold")

for c in t:
    for cc in mp[c]:
        bg[c] += cc[1]*bg[cc[0]]+cc[1]

print(bg["shiny gold"])
