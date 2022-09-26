"""
    Subset using recursion
"""

subs = []
def subset(res, arr):
    if len(arr) == 0:
        subs.append(res)
        return 
    char = arr[0]
    subset(res + str(char), arr[1:])
    subset(res, arr[1:])

subset('', [1, 2, 3, 4, 5])

print(subs)