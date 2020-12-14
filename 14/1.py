import sys

input = [x.strip().replace(" ", "").split("=") for x in sys.stdin]

mp = {}

om = 0
xm = 0
for (a,b) in input:
    if a == "mask":
        om = 0
        xm = 0
        for j in range(0, len(b)):
            if b[j] == '1':
                om |= (1<<(len(b)-j-1))
            elif b[j] == '0':
                xm |= (1<<(len(b)-j-1))
        xm = ~xm
    else:
        mp[int(a[4:-1])] = (om|int(b))&xm
print(sum(mp.values()))
