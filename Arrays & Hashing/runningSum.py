"""
    1480. Running Sum of 1d Array
    - LeetCode
"""

nums = list(map(int, input().split(',')))
runningSum = []
for i in range(1, len(nums) + 1):
    runningSum.append(sum(nums[:i]))

print(runningSum)