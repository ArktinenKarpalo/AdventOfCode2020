import sys
import itertools

input = [x.strip().split("(") for x in sys.stdin]

it = set()

ai = {}

itt = []

for i in input:
    ingredients = i[0][:-1].split(" ")
    itt += ingredients
    for g in ingredients:
        it.add(g)
    allergens = list(map(lambda x: x.strip(), i[1][9:-1].split(",")))
    for a in allergens:
        if a in ai:
            ai[a] = ai[a].intersection(ingredients)
        else:
            ai[a] = set()
            ai[a] |= set(ingredients)
ans = []
while len(ai) > 0:
    d = None
    for k,v in ai.items():
        if len(v) == 1:
            ans.append((k,list(v)[0]))
            for k2,v2 in ai.items():
                if k2 == k:
                    continue
                v2 -= v
            d = k
            break
    del ai[d]
ans.sort()
print(",".join(map(lambda x: x[1], ans)))
