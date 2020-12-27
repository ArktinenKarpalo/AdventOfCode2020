import sys

prog = [(lambda x: (x[0], int(x[1])))(x.strip().split()) for x in sys.stdin]
vis = [0]*len(prog)

pc = 0
acc = 0

while vis[pc] == 0:
    vis[pc] += 1
    if prog[pc][0] == "acc":
        acc += prog[pc][1]
        pc += 1
    elif prog[pc][0] == "jmp":
        pc += prog[pc][1]
    elif prog[pc][0] == "nop":
        pc += 1
print(acc)
