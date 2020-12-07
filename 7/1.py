import sys
import collections
import re
import queue

mp = collections.defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    color = re.match("(.*?) bags?", line).group(1)
    contents = re.findall("([0-9]+) ([^,.]+) bags?", line)
    for bag in contents:
        mp[bag[1]].append(color)

vis = set()
q = queue.Queue()
q.put("shiny gold")
while not q.empty():
    cur = q.get()
    for c in mp[cur]:
        q.put(c)
    vis.add(cur)

print(len(vis)-1)
