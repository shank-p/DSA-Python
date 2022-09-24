
nums = [1, 2, 3, 4]

lonely = []
for i in range(1, len(nums)-1):
    if abs(nums[i]-nums[i+1])==1 or abs(nums[i] - nums[i-1])==1:
        continue
    else:
        lonely.append(nums[i])

"""
for i in nums:
    if i+1 not in nums or i-1 not in nums or nums.count(i)==1 : append to list
"""

print(lonely)