"""
    724. Find Pivot Index
    - LeetCode
"""

nums = list(map(int, input().split(',')))

for i in range(len(nums)):
    if (sum(nums[:i]) == sum(nums[i:])-nums[i]):
        print(i)
        break


""" Reduced complexity
"""
total = sum(nums)
left_sum = 0
for i in range(len(nums)):
    if (left_sum == (total - left_sum - nums[i])):
        print(i)
    else:
        left_sum += nums[i]


