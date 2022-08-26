"""
    34. Find First and Last Position of Element in Sorted Array
    - leetCode
"""

nums = list(map(int, input().split()))
target = int(input())

def search(nums, target, isFirst):
    low = 0
    high = len(nums) - 1
    ans = -1

    while(low <= high):
        mid = (low+high)//2
        if (nums[mid] < target):
            low = mid + 1
        elif (nums[mid] > target):
            high = mid - 1
        else:
            ans = mid
            if (isFirst):
                high = mid - 1
            else:
                low = mid + 1
    return ans
first = search(nums, target, True)
last = search(nums, target, False)
print([first, last])