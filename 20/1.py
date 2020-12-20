import sys
import numpy
import collections

input = map(lambda x: x.split("\n"), "".join(list(sys.stdin))[:-1].split("\n\n"))
input = list(map(lambda x: {"id": int(x[0][-5:-1]), "grid": numpy.array(list(map(list, x[1:])))}, input))

ss = collections.defaultdict(set)
for g in input:
    ss[str(g["grid"][:,0])].add(g["id"])
    ss[str(g["grid"][:,9])].add(g["id"])
    ss[str(g["grid"][0,:])].add(g["id"])
    ss[str(g["grid"][9,:])].add(g["id"])
    ss[str(g["grid"][:,0][::-1])].add(g["id"])
    ss[str(g["grid"][:,9][::-1])].add(g["id"])
    ss[str(g["grid"][0,:][::-1])].add(g["id"])
    ss[str(g["grid"][9,:][::-1])].add(g["id"])

ans = 1

for g in input:
    cnt = 0
    if len(ss[str(g["grid"][:,0])]) == 1 and len(ss[str(g["grid"][:,0][::-1])]) == 1:
        cnt += 1
    if len(ss[str(g["grid"][:,9])]) == 1 and len(ss[str(g["grid"][:,9][::-1])]) == 1:
        cnt += 1
    if len(ss[str(g["grid"][0,:][::-1])]) == 1 and len(ss[str(g["grid"][0,:])]) == 1:
        cnt += 1
    if len(ss[str(g["grid"][9,:])]) == 1 and len(ss[str(g["grid"][9,:][::-1])]) == 1:
        cnt += 1
    if cnt == 2:
        print(g["id"])
        ans *= g["id"]
print(ans)
