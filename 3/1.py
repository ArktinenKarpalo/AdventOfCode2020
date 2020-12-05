import sys

ans = 0
x = 0

for line in sys.stdin:
    if line[x] == '#':
        ans += 1
    x += 3
    x %= len(line)-1 # Contains newline in the end
print(ans)

