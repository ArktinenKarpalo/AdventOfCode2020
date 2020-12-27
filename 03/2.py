import sys

def trees(right, down, lines):
    x = 0
    ans = 0
    for i in range(0, len(lines), down):
        if lines[i][x] == '#':
            ans += 1
        x += right
        x %= len(lines[i])-1 # Contains newline in the end
    return ans



lines = []
for line in sys.stdin:
    lines.append(line)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
ans = 1
for slope in slopes:
    ans *= trees(*slope, lines)
print(ans)

