"""
    Bubble Sort algorithm
"""

nums = list(map(int, input().split()))

def swap(a,b, nums):
    if nums[a]>nums[b]:
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

for i in range(len(nums)-1):
    for j in range(0, len(nums)-1-i):
        swap(j, j+1, nums)
    print(nums)

print(nums)