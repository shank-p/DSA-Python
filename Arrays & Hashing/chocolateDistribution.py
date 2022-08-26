"""
    Chocolate Distribution Problem
    - GFG
"""

arr = list(map(int, input().split(',')))
students = int(input())

arr.sort()
print(arr)
min = 999
for i in range(len(arr) - students + 1):
    print('i val :', i)
    difference = abs(arr[i]-arr[i+students - 1])
    print('diff val : ', difference)
    if difference < min:
        min = difference
    print('min val : ', min)
print(min)
    
"""
"""
arr = list(map(int, input().split(',')))
m = int(input())

arr.sort()
print(arr)

minSum = 999
for i in range(0, len(arr)-m+1):
    pack1 = arr[i]
    packm = arr[i+m-1]
    differ = packm - pack1
    print('d', differ)
    minSum = min(minSum, differ)
    print('m', minSum)
print(minSum)