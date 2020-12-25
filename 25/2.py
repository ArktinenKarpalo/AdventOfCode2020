import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

M = 20201227

num = 7
for i in range(M):
    num *= 7
    num %= M
    if num == A:
        n2 = B
        for j in range(i+1):
            n2 *= B
            n2 %= M
        print(n2)
        break
    elif num == B:
        n2 = A
        for j in range(i+1):
            n2 *= A
            n2 %= M
        print(n2)
        break

