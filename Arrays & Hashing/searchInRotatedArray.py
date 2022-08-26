"""
    Search an element in a sorted and rotated array
    - GFG
"""

arr = list(map(int, input().split(',')))
key = int(input())

low = 0
high = len(arr) - 1
found = False
while(low <= high):
    mid = (low + high)//2
    if (arr[mid] == key): 
        print(mid)
        found = True
        break
    elif (arr[mid] > key):
        if (arr[low] > key):
            low = mid + 1
        else:
            high  = mid - 1
    elif (arr[mid] < key):
        if (key > arr[high]):
            high = mid - 1
        else:
            low = mid + 1

if (found == False ):
    print(-1)

"""
---------------------------------------------------------------------------------------------------------
"""

nums = list(map(int, input().split()))
target = int(input())

def findPivot(arr):
    low = 0
    high = len(arr) - 1

    while(low < high):
        mid = (low + high)//2
        if (mid < high and arr[mid] > arr[mid + 1]):
            return mid
        elif (mid > low and arr[mid] < arr[mid - 1]):
            return mid - 1
        elif (arr[mid] <= arr[low]):
            high = mid - 1
        else:
            low = mid
    return(-1)

def binarySearch(start, end, target, nums):
    low = start
    high = end
    while(low <= high):
        mid = (low + high)//2
        if (nums[mid] < target):
            low = mid + 1
        elif (nums[mid] > target):
            high = mid - 1
        else:
            return(mid)
    return(-1)

pivot = findPivot(nums)
print(pivot)
if (pivot == -1):
    ans = binarySearch(0, len(nums)-1, target, nums)
elif (nums[pivot] == target):
    ans = pivot
elif (target >= nums[0]):
    ans = binarySearch(0, pivot, target, nums)
else:
    ans = binarySearch(pivot + 1, len(nums)-1, target, nums)

print(ans)
