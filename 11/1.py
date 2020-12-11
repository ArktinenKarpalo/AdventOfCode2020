import sys
import copy

input = [list("."*101)]
input += [list("."+x.strip()+".") for x in sys.stdin]
input.append(list("."*101))

i2 = copy.deepcopy(input)

def adj(x, y):
    return sum(input[x+i][y-1:y+2].count("#") for i in range(-1,2))

def ok(x, y):
    if input[x][y] == '.':
        return False
    elif input[x][y] == '#':
        if adj(x,y) >= 5:
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
print(cnt())
