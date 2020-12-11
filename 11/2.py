import sys
import copy

input = [list("L"*101)]
input += [list("L"+x.strip()+"L") for x in sys.stdin]
input.append(list("L"*101))

i2 = copy.deepcopy(input)

def nfree(x, y, xofs, yofs):
    while True:
        x += xofs
        y += yofs
        if input[x][y] == '#':
            return True
        elif input[x][y] == 'L':
            return False
    return nfree(x+xofs, y+yofs, xofs, yofs)

ofs = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
    (1,1),
    (-1,-1),
    (1,-1),
    (-1,1)
]

def adj(x, y):
    return sum(nfree(x, y, *o) for o in ofs);

def ok(x, y):
    if input[x][y] == '.':
        return False
    elif input[x][y] == '#':
        if adj(x, y) >= 5:
            i2[x][y] = 'L'
            return False
        return True
    else:
        if adj(x,y) == 0:
            i2[x][y] = '#'
            return True
        return False

def cnt():
    cnt = 0
    for x in range(1,len(input)-1):
        for y in range(1,len(input[1])-1):
            cnt += ok(x,y)
    return cnt

last = -1
while (new := cnt()) != last:
    input = copy.deepcopy(i2)
    last = new
print(last)
