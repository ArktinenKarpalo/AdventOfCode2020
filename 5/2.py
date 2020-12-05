import sys

sum = 0
mi = 1e9
mx = 0
for line in sys.stdin:
    row = 0
    for i in range(0,7):
        if line[i] != 'F':
            row |= (1<<(6-i))

    col = 0
    for i in range(0,3):
        if line[7+i] != 'L':
            col |= (1<<(2-i))
    id = row*8+col
    sum += id
    mi = min(mi, id)
    mx = max(mx, id)
print(int(((mx*(mx+1))/2)-(mi*(mi+1))/2-sum))
