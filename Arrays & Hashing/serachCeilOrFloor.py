"""
    Find the ceil of a terget in an arr.
    # ceil of target is : smallest number greater than or equal to (>=) target

    Find the floor of a terget in an arr.
    # floor of target is : greatest number smaller than or equal to (<=) target

"""

arr = list(map(int, input().split()))
target = int(input())

#floor search
def FloorSearch(nums, target):
    low = 0
    high = len(nums) - 1
    while (low<high):
        mid = (low + high)//2
        if (arr[mid] == target):
            floor = target
            return(floor)
        elif (arr[mid] < target):
            low  = mid + 1
        else:
            high = mid - 1
    return (low)

ans = FloorSearch(arr, target)
if (arr[ans] < target):
    print(-1)
else:
    print(arr[ans])
