import sys

nums = []
for line in sys.stdin:
    cur = int(line)
    nums.append(cur)
nums.sort()
for i in range(1, len(nums)):
    k = len(nums)-1
    for j in range(i+1, len(nums)):
        while nums[i]+nums[j]+nums[k] > 2020 and k > 0:
            k-=1
        if nums[i]+nums[j]+nums[k] == 2020:
            print(nums[i]*nums[j]*nums[k])
