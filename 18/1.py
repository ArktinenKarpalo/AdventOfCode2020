import sys

input = list(map(lambda x: x.strip().replace(" ", ""), sys.stdin))


ans = 0

op = []
num = []

def proc():
    while len(num) >= 2:
        if op[len(op)-1] != '(':
            o = op.pop()
            if o == '*':
                num.append(num.pop() * num.pop())
            elif o == '+':
                num.append(num.pop() + num.pop())
        else:
            break

for line in input:
    num = []
    op = []
    for c in line:
        if c >= '0' and c <= '9':
            num.append(int(c))
        elif c == '+':
            proc()
            op.append(c)
        elif c == '*':
            proc()
            op.append(c)
        elif c == '(':
            op.append(c)
        elif c == ')':
            proc()
            op.pop()
            proc()
    proc()
    ans += num[0]


print(ans)
