import sys

input = [int(x) for x in sys.stdin]
input.sort()
jolts = [0]*(input[len(input)-1]+1)
jolts[0] = 1

for i in input:
    jolts[i] = sum(jolts[max(i-3, 0):i])

print(jolts[input[len(input)-1]])
