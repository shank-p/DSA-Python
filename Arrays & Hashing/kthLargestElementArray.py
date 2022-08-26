"""
    215. Kth Largest Element in an Array
    - leetcode
"""

nums = list(map(int, input().split(',')))
k = int(input())

#nums = list(set(nums))
nums.sort()

print(nums)
