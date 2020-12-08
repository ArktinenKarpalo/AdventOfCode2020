import sys

prog = [(lambda x: (x[0], int(x[1])))(x.strip().split()) for x in sys.stdin]
vis = [0]*len(prog)

pc = 0
acc = 0

ok = [0]*len(prog)

for i in range(len(prog)):
    cvis = []
    terminates = False
    pc = i
    while vis[pc] == 0:
        cvis.append(pc)
        vis[pc] += 1
        if prog[pc][0] == "acc":
            pc += 1
        elif prog[pc][0] == "jmp":
            pc += prog[pc][1]
        elif prog[pc][0] == "nop":
            pc += 1
        if pc >= len(prog) or ok[pc]:
            terminates = True
            break
    if terminates:
        for el in cvis:
            ok[el] = True

chg = False
pc = 0
while pc < len(prog):
    if prog[pc][0] == "acc":
        acc += prog[pc][1]
        pc += 1
    elif prog[pc][0] == "jmp":
        if not chg and (pc+1 >= len(prog) or ok[pc+1]):
            chg = True
            pc += 1
        else:
            pc += prog[pc][1]
    elif prog[pc][0] == "nop":
        if not chg and (pc+prog[pc][1] >= len(prog) or ok[pc+prog[pc][1]]):
            chg = True
            pc += prog[pc][1]
        else:
            pc += 1
print(acc)
