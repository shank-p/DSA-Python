"""
    2357. Make Array Zero by Subtracting Equal Amounts
    - leetCode
"""

nums = list(map(int, input().split()))

count = 0
nums.sort()
while(sum(nums) > 0):
    zeroIndex = nums.count(0)
    if zeroIndex != 0:
        nums = nums[zeroIndex:]
    nums = [i-nums[0] for i in nums]
    print(nums)
    count += 1
print(count)

"""
"""
#               :(
print(len(set(nums)) - nums.count(0)) 