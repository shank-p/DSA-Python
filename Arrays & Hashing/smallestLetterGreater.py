"""
    744. Find Smallest Letter Greater Than Target
    - leetcode
"""

letters = input().split()
n = len(letters)
target = input()

def search(arr, target):
    low = 0
    high = n -1
    while(low<=high):
        mid = (low + high)//2
        if(arr[mid] == target):
            next = mid + 1
            return(next)
        elif (arr[mid] < target):
            low = mid + 1
        else:
            high = mid -1
    return(low)

ans = search(letters, target)
ans = ans % n
print(letters[ans])