"""
    Maximum and minimum of an array using minimum number of comparisons
    - GFG
"""

arr = list(map(int, input().split()))

# Linear
min1 = max1 = arr[0]
for i in arr:
    if (i < min1 ):
        min1 = i
    elif (i > max1):
        max1 = i
print(min1, max1)


# Tournament Method (divide arr by 2, find min and max in each of those arrays)


# Compare in pairs
if (len(arr) %2 == 0):
    min_no = min(arr[0], arr[1])
    max_no = max(arr[0], arr[1])
    start = 2
else:
    min_no = max_no = arr[0]
    start = 1

for i in range(start, len(arr), 2):
    if (arr[i] <= arr[i+1]):
        if (min_no > arr[i]):
            min_no = arr[i]
        if (max_no < arr[i+1]):
            max_no = arr[i+1]
    else:
        if (min_no > arr[i + 1]):
            min_no = arr[i + 1]
        if (max_no < arr[i]):
            max_no = arr[i]
print(min_no, max_no)