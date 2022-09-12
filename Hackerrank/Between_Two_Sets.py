"""
    Between Two Sets
    -Hackerrank
"""

def getTotal(arr1, arr2):
    res=0
    for i in range(max(arr1),min(arr2)+1):
        if all(i%x==0 for x in arr1) and all(x%i==0 for x in arr2):
            res+=1
    return res


no_of_ele = list(map(int, input().split()))
m = no_of_ele[0]
n = no_of_ele[1]

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = getTotal(arr1, arr2)
print(result)