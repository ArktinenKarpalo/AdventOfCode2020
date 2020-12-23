import sys

class Node:
    def __init__(self, el, next, prev):
        if next == None:
            self.next = self
            self.prev = self
        else:
            self.next = next
            self.prev = prev
        self.el = el
    def append(self, el):
        self.next.prev = Node(el, self.next, self)
        self.next = self.next.prev
        return self.next

input = list(map(int, sys.stdin.readline().strip()))

c_n = [None]*(len(input)+1)

for i in range(len(input)):
    if i == 0:
        c_n[input[i]] = Node(input[i], None, None)
    else:
        c_n[input[i]] = c_n[input[i-1]].append(input[i])

cur = c_n[input[0]]

for i in range(100):
    s = cur.next
    e = cur.next.next.next
    cur.next = e.next
    e.next.prev = cur
    dest = cur.el-1
    if dest == 0:
        dest = len(input)
    while dest == s.el or dest == s.next.el or dest == s.next.next.el:
        dest = dest-1
        if dest == 0:
            dest = len(input)
    c_n[dest].next.prev = e
    e.next = c_n[dest].next
    c_n[dest].next = s
    s.prev = c_n[dest]
    cur = cur.next

ans = ""
cur = c_n[1]
for i in range(len(input)-1):
    cur = cur.next
    ans += str(cur.el)

print(ans)
