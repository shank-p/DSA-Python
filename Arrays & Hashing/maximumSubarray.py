"""
    53. Maximum Subarray
    - LeetCode
"""
nums = list(map(int, input().split(',')))

maxSum = nums[0]
curSum = 0
for i in nums:
    if (curSum < 0):
        curSum = 0
    curSum += i
    maxSum = max(maxSum, curSum)
print(maxSum)