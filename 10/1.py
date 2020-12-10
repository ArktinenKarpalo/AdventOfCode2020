import sys

input = [int(x) for x in sys.stdin]
input.sort()
jd = [0]*4
jd[3] = 1
jd[input[0]] += 1

for i in range(1,len(input)):
    jd[input[i]-input[i-1]] += 1

print(jd[1]*jd[3])
