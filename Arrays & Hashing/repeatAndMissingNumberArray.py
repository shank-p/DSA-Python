"""
    Repeat and Missing Number Array
    - InterviewBit
"""

arr = list(map(int, input().split()))
n = len(arr)

actualSum = (n*(n+1))//2
givenSum = sum(arr)

arr.sort()
for i in range(1, len(arr)):
    if arr[i-1] == arr[i]:
        r = arr[i]
        break

differ = abs(actualSum - givenSum)
if (actualSum > givenSum):
    m = differ + r
else:
    m = r - differ
print(m, r)

"""
"""

arr = list(map(int, input().split()))
n = len(arr)

actualSum = (n*(n+1))//2
squareSum = (n*(n+1)*(2*n+1))//6
givenSum = sum(arr)

linear = abs(actualSum-givenSum)

