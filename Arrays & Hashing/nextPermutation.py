"""
    31. Next Permutation
    - leetCode
"""

nums = list(map(int, input().split()))

def swap (a, b, nums=nums):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp

if(len(nums) < 2):
    exit()

done = False
mSig = -2
while(not done):
    if (mSig == -(len(nums)+1)):
        nums.sort()
        break
    for i in range(-1, mSig, -1):
        print(i, mSig)
        if (nums[i] > nums[mSig]):
            swap(i, mSig)
            print(mSig)
            nums = nums[:mSig+1] + sorted(nums[mSig+1:])
            done = True
            break
    mSig -= 1
print(nums)