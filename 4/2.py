import sys
import itertools
import re

global validators
validators = {
    "byr": lambda x: (int(x) >= 1920 and int(x) <= 2002),
    "iyr": lambda x: (int(x) >= 2010 and int(x) <= 2020),
    "eyr": lambda x: (int(x) >= 2020 and int(x) <= 2030),
    "hgt": lambda x: ((x[-2:] == "cm" and int(x[:-2]) >= 150 and int(x[:-2]) <= 193) or (x[-2:] == "in" and int(x[:-2]) >= 59 and int(x[:-2]) <= 76)),
    "hcl": lambda x: (re.match("#[0-9a-f]{6}$", x) != None),
    "ecl": lambda x: (re.match("amb|blu|brn|gry|grn|hzl|oth$", x) != None),
    "pid": lambda x: (re.match("[0-9]{9}$", x) != None),
    "cid": lambda x: True
}

def valid(fields):
    for x in current:
        if x.startswith("cid:"):
            if len(fields) != 8:
                return False
        else:
            kv = x.split(":")
            if validators[kv[0]](kv[1]) == False:
                return False
    if len(fields) < 7:
        return False
    return True
ans = 0

current = []
for line in sys.stdin:
    if line == "\n":
        ans += valid(current)
        current = []
    else:
        current.extend(line.split())
ans += valid(current)
print(ans)
