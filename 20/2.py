import sys
import math
import numpy
import random
import collections

def rot(grid, k):
    return numpy.rot90(grid, k)
def flip(grid, a):
    return numpy.flip(grid, a)

input = map(lambda x: x.split("\n"), "".join(list(sys.stdin))[:-1].split("\n\n"))
input = list(map(lambda x: {"id": int(x[0][-5:-1]), "grid": numpy.array(list(map(list, x[1:])))}, input))

br = set()
ss = collections.defaultdict(set)
for g in input:
    ss[str(g["grid"][:,0])].add(g["id"])
    ss[str(g["grid"][:,9])].add(g["id"])
    ss[str(g["grid"][0,:])].add(g["id"])
    ss[str(g["grid"][9,:])].add(g["id"])
    ss[str(g["grid"][:,0][::-1])].add(g["id"])
    ss[str(g["grid"][:,9][::-1])].add(g["id"])
    ss[str(g["grid"][0,:][::-1])].add(g["id"])
    ss[str(g["grid"][9,:][::-1])].add(g["id"])

for g in input:
    cnt = 0
    if len(ss[str(g["grid"][:,0])]) == 1 and len(ss[str(g["grid"][:,0][::-1])]) == 1:
        br.add(g["id"])
    if len(ss[str(g["grid"][:,9])]) == 1 and len(ss[str(g["grid"][:,9][::-1])]) == 1:
        br.add(g["id"])
    if len(ss[str(g["grid"][0,:][::-1])]) == 1 and len(ss[str(g["grid"][0,:])]) == 1:
        br.add(g["id"])
    if len(ss[str(g["grid"][9,:])]) == 1 and len(ss[str(g["grid"][9,:][::-1])]) == 1:
        br.add(g["id"])

z = set()
g = {}

ans = {}
N = 12
def qaq(x, y, id):
    if id in br:
        if not(x == 1 or x == N or y == N or y == 1):
            return False
    elif(x == 1 or x == N or y == N or y == 1):
        return False
    if (x-1, y) in g and not (numpy.array_equiv(g[(x-1, y)][:,9], g[(x,y)][:,0])):
        return False
    if (x, y-1) in g and not (numpy.array_equiv(g[(x, y-1)][9,:], g[(x,y)][0,:])):
        return False
    if x == N and y == N:
        return True
    for tile in input:
        for r in range(0, 4):
            for f in range(0, 3):
                if tile["id"] in z:
                    continue
                if x == N:
                    z.add(tile["id"])
                    gr = tile["grid"]
                    if r > 0:
                        gr = rot(gr, r)
                    if f < 2:
                        gr = flip(gr, f)
                    elif f == 3:
                        gr = flip(gr, 0)
                        gr = flip(gr, 1)
                    g[(1, y+1)] = gr
                    if qaq(1, y+1, tile["id"]):
                        ans[(1,y+1)] = gr
                        return True
                    del g[(1,y+1)]
                    z.remove(tile["id"])
                else:
                    z.add(tile["id"])
                    gr = tile["grid"]
                    if r > 0:
                        gr = rot(gr, r)
                    if f < 2:
                        gr = flip(gr, f)
                    elif f == 3:
                        gr = flip(gr, 0)
                        gr = flip(gr, 1)
                    g[(x+1, y)] = gr
                    if qaq(x+1, y, tile["id"]):
                        ans[(x+1,y)] = gr
                        return True
                    del g[(x+1,y)]
                    z.remove(tile["id"])
    return False


tl = {}
for i in input:
    tl[i["id"]] = i["grid"]
def grid():
    for tile in input:
        if tile["id"] != 2693: # Start from a guaranteed corner
            continue
        for r in range(0,4):
            for f in range(0,3):
                z.add(tile["id"])
                gr = tile["grid"]
                if r > 0:
                    gr = rot(gr, r)
                if f < 2:
                    gr = flip(gr, f)
                elif f == 3:
                    gr = flip(gr, 0)
                    gr = flip(gr, 1)
                g[(1, 1)] = gr
                if qaq(1,1,tile["id"]):
                    ans[(1,1)] = gr
                    return
                del g[(1,1)]
                z.remove(tile["id"])
im = [[] for i in range(12*8)]
grid()
for i in range(1, 13):
    for j in range(1, 13):
        for k in range(1,9):
            im[j*8+k-9] += list(ans[(i,j)][k,:][1:-1])
mo = [
    (18,2),
    (0,1),
    (5,1),
    (6,1),
    (11,1),
    (12,1),
    (17,1),
    (18,1),
    (19,1),
    (1,0),
    (4,0),
    (7,0),
    (10,0),
    (13,0),
    (16,0)
]

def cm(grid):
    for i in range(0, len(grid)-19):
        for j in range(0, len(grid)-2):
            ok = True
            for ofs in mo:
                if grid[i+ofs[0]][j+ofs[1]] == '.':
                    ok = False
                    continue
            if ok:
                for ofs in mo:
                    grid[i+ofs[0]][j+ofs[1]] = 'O'

for r in range(0,4):
    im = rot(im, r)
    cm(im)
    im = flip(im, 0)
    cm(im)
    im = flip(im, 0)
    im = flip(im, 1)
    cm(im)
for r in im:
    print("".join(r))
print(sum(map(lambda x: list(x).count('#'), im)))
