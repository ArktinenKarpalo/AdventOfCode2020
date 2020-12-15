import sys
import collections

input = list(map(int, sys.stdin.readline().strip().split(",")))

ls = collections.defaultdict(int)

x = -1
for i in range(0, len(input)):
    ls[x] = i
    x = input[i]
for i in range(len(input), 2020):
    if ls[x] == 0:
        ls[x] = i
        x = 0
    else:
        p = x
        x = i-ls[x]
        ls[p] = i
print(x)
