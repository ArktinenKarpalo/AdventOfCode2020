import sys

ans = 0

for line in sys.stdin:
    row = 0
    for i in range(0,7):
        if line[i] != 'F':
            row |= (1<<(6-i))

    col = 0
    for i in range(0,3):
        if line[7+i] != 'L':
            col |= (1<<(2-i))
    ans = max(ans, row*8+col)
print(ans)

