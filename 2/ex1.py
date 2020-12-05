import sys

ans = 0

for line in sys.stdin:
    sep = line.find("-")
    least = int(line[:sep])
    sep2 = line.find(":")
    most = int(line[sep+1:sep2-1])
    valid_char = line[sep2-1:sep2]
    valid_chars = 0
    for char in line[sep2:]:
        if char == valid_char:
            valid_chars+=1
    if valid_chars >= least and valid_chars <= most:
        ans += 1

print(ans)

