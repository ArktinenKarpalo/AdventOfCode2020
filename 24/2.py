import sys

black = set()
for line in sys.stdin:
    line = line.strip()
    x = y = 0
    for i in range(len(line)):
        if line[i] == 'e' and (i == 0 or (line[i-1] != 'n' and line[i-1] != 's')):
            x += 1
        elif line[i] == 'w' and (i == 0 or (line[i-1] != 'n' and line[i-1] != 's')):
            x -= 1
        elif line[i:i+2] == 'se':
            y -= 1
            x += 1
        elif line[i:i+2] == 'sw':
            y -= 1
        elif line[i:i+2] == 'ne':
            y += 1
        elif line[i:i+2] == 'nw':
            y += 1
            x -= 1
    if (x,y) in black:
        black.remove((x,y))
    else:
        black.add((x,y))
adj = [(1,0), (-1,0),(1,-1),(0,1),(0,-1),(-1,1)]

def ne(x,y):
    for ofs in adj:
        yield (x+ofs[0],y+ofs[1])

def bn(x,y):
    ret = 0
    for g in ne(x,y):
        if g in black:
            ret += 1
    return ret

for i in range(100):
    new_black = set()
    for tile in black:
        if (neig := bn(*tile)) == 1 or neig == 2:
            new_black.add(tile)
        for n in ne(*tile):
            if n not in black and bn(*n) == 2:
                new_black.add(n)
    black = new_black

print(len(black))

