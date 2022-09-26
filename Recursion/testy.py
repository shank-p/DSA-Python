
nums = list(map(int, input().split()))

def mergeSort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:len(arr)])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0 #left arr index 
    j = 0 # right arr index

    while(i<len(left) and j<len(left)):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        print(result)
    
    while(i<len(left)):
        result.append(left[i])
        i += 1
    while(j<len(right)):
        result.append(right[j])
        j += 1
    
    return result

ans = mergeSort(nums)
print(ans)