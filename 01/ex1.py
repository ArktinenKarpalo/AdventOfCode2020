import sys

nums = set()
for line in sys.stdin:
    cur = int(line)
    if 2020-cur in nums:
        print(cur*(2020-cur))
    nums.add(cur)

