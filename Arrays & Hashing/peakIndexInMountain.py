"""
    852. Peak Index in a Mountain Array
    - leetCode
"""

arr = list(map(int, input().split()))

def search(arr):
    low = 0
    high = len(arr) - 1
    while(low < high):
        mid = (low + high)//2
        if (arr[mid] < arr[mid + 1]):
            # ascending part
            low = mid + 1
        else:
            high = mid 
    return low
print(search(arr))