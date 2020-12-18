import sys

input = list(map(lambda x: x.strip().replace(" ", ""), sys.stdin))


ans = 0

op = []
num = []

def proc(c):
    while len(num) >= 2:
        if op[len(op)-1] != '(':
            o = op.pop()
            if o == '*' and c != '+':
                num.append(num.pop() * num.pop())
            elif o == '+':
                num.append(num.pop() + num.pop())
            else:
                op.append(o)
                break
        else:
            break

for line in input:
    num = []
    op = []
    for c in line:
        if c >= '0' and c <= '9':
            num.append(int(c))
        elif c == '+':
            proc(c)
            op.append(c)
        elif c == '*':
            proc(c)
            op.append(c)
        elif c == '(':
            op.append(c)
        elif c == ')':
            proc(c)
            op.pop()
            proc("+")
    proc("")
    ans += num[0]


print(ans)
