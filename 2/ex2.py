import sys

ans = 0

for line in sys.stdin:
    sep = line.find("-")
    sep2 = line.find(":")
    least = int(line[:sep])
    most = int(line[sep+1:sep2-1])
    positions = [least, most]
    valid_char = line[sep2-1:sep2]
    valid_chars = 0
    for idx in positions:
        if line[sep2+1+idx] == valid_char:
            valid_chars+=1
    if valid_chars == 1:
        ans += 1

print(ans)

