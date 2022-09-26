"""
    Merge Sort Algorithm
"""

arr = list(map(int, input().split()))

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:len(arr)])
    return merge(left, right)

def merge(left, right):
    sorted = []
    i = 0   #left index
    j = 0   #right index

    while(i<len(left) and j<len(right)):
        if (left[i] < right[j]):
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    
    # if len of 1 arr is greater than other
    # only 1 while loop will run
    while(i< len(left)):
        sorted.append(left[i])
        i += 1
    while(j< len(right)):
        sorted.append(right[j])
        j += 1
    
    return sorted

result = mergeSort(arr)
print(result)
    





