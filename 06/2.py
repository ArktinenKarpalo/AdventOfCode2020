import sys
import collections

yes = collections.defaultdict(int)
ans = 0
gl = 0
for line in sys.stdin:
    if len(line) == 1:
        for k in yes.values():
            if k == gl:
                ans += 1
        gl = 0
        yes.clear()
    else:
        gl += 1
        for c in line.strip():
            yes[c] += 1
for k in yes.values():
    if k == gl:
        ans += 1
print(ans)
