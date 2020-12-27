import sys

nums = [int(x.strip()) for x in sys.stdin]

ans = 0
for i in range(len(nums)):
    if i < 25:
        continue
    ok = False
    for j in range(i-25, i+1):
        for k in range(i-25, i+1):
            if i == k:
                continue
            if nums[j]+nums[k] == nums[i]:
                ok = True
    if not ok:
        ans = nums[i]
        break
l = 0
r = 0
sum = nums[0]
while r < len(nums):
    r += 1
    sum += nums[r]
    while r-l > 1 and sum > ans:
        sum -= nums[l]
        l += 1
    if sum == ans:
        print(min(nums[l:r])+max(nums[l:r]))
        break
