"""
    1470. Shuffle the Array
    - leetcode
"""

nums = list(map(int, input().split()))
halfLen = len(nums)//2
# arr always even as given arr len is 2n

j = 0
for i in range(0, len(nums), 2):
    temp = nums[halfLen + j]
    nums.pop(halfLen + j)
    nums.insert(i+1, temp)
    j += 1
print(nums)
