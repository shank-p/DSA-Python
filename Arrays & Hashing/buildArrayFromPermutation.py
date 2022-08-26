"""
    1920. Build Array from Permutation
    - leetcode
"""

nums = list(map(int, input().split(',')))
ans = []

for i in nums:
    ans.append(nums[i])

print(ans)