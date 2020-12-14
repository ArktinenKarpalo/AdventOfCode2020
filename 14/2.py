import sys

input = [x.strip().replace(" ", "").split("=") for x in sys.stdin]

mp = {}

x = []
os = 0
zs = 0
for (a,b) in input:
    if a == "mask":
        b = list(b)
        b.reverse()
        x = []
        os = 0
        zs = 0
        for i in range(0, len(b)):
            if b[i] == 'X':
                x.append(i)
            elif b[i] == '0':
                zs |= (1<<i)
            else:
                os |= (1<<i)

    else:
        for i in range(0, 1<<len(x)):
            xm = 0
            for j in range(0, len(x)):
                if (i&(1<<j)) != 0:
                    xm |= (1<<x[j])
            mp[((int(a[4:-1])&zs)|os)|xm] = int(b)
print(sum(mp.values()))
