import sys

class Node:
    def __init__(self, el, next):
        if next == None:
            self.next = self
        else:
            self.next = next
        self.el = el
    def append(self, el):
        self.next = Node(el, self.next)
        return self.next

input = list(map(int, sys.stdin.readline().strip()))
for i in range(len(input)+1, 1000000+1):
    input.append(i)

c_n = [None]*(len(input)+1)

for i in range(len(input)):
    if i == 0:
        c_n[input[i]] = Node(input[i], None)
    else:
        c_n[input[i]] = c_n[input[i-1]].append(input[i])

cur = c_n[input[0]]

for i in range(10000000):
    s = cur.next
    e = cur.next.next.next
    cur.next = e.next
    dest = cur.el-1
    if dest == 0:
        dest = len(input)
    while dest == s.el or dest == s.next.el or dest == s.next.next.el:
        dest = dest-1
        if dest == 0:
            dest = len(input)
    e.next = c_n[dest].next
    c_n[dest].next = s
    cur = cur.next

cur = c_n[1]
print(cur.next.el*cur.next.next.el)
