"""
    Sum triangle from array
    - GFG
"""

arr = list(map(int, input().split()))

def sumTriangle(arr):
    if len(arr) == 1:
        print(arr)
        return
    temp = [arr[i] + arr[i+1] for i in range(len(arr)-1)]
    sumTriangle(temp)
    print(arr)

sumTriangle(arr)