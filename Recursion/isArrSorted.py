"""
    Check if aan arr is sorted in ascending order using recursion
"""

nums = [1, 2, 4, 5, 9, 12]

def check(nums):
    if len(nums) == 1:
        return True
    return nums[0]<nums[1] and check(nums[1:])
res = check(nums)
print(res)