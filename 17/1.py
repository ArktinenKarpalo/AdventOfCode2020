import sys
import operator as op

cubes = set()
x = 0
for line in sys.stdin:
    line = line.strip()
    for j in range(len(line)):
        if line[j] == '#':
            cubes.add((x,j,0))
    x += 1

ofs = []

for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            if i == j and j == k and i == 0:
                continue
            ofs.append((i, j, k))

def neighbors(c, cubes):
    ret = 0
    for o in ofs:
        if tuple(map(op.add, c, o)) in cubes:
            ret += 1
    return ret


def sim(cubes):
    new_cubes = set()
    for cube in cubes:
        n = neighbors(cube, cubes)
        if n == 2 or n == 3:
            new_cubes.add(cube)
        for o in ofs:
            if neighbors(tuple(map(op.add, cube,o)), cubes) == 3:
                new_cubes.add(tuple(map(op.add, cube,o)))
    return new_cubes

for i in range(6):
    cubes = sim(cubes)

print(len(cubes))
