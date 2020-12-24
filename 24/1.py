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
print(len(black))

