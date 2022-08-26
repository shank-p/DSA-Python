"""
    - Bubble Sort
"""

nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    swapped = False
    for j in range(0, len(nums)-i):
        if (nums[j] > nums[j+1]):
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            swapped = True
    if (not swapped):
        break
print(nums)