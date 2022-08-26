"""
    217. Contains Duplicate
    - LeetCode
"""

nums = list(map(int, input().split()))

hash = []
for i in nums:
    if i not in hash:
        hash.append(i)
    else:
        print('True')
        exit()
print('False')