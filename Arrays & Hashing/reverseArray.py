"""
    program to reverse an array or string
    - GFG
"""

arr = list(map(int, input().split()))
# arr[::-1]

# swap the nums at the ends
n = len(arr)
for i in range(len(arr)//2):
    temp = arr[i]
    arr[i] = arr[n-1 - i]
    arr[n-1 -i] = temp
print(arr)