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
for i in ai.values():
    it -= i
print(sum(1 for x in itt if x in it))

