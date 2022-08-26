"""
    1. Two Sum
    - LeetCode
"""

nums = list(map(int, input().split()))
target = int(input())

table = {}
for index, element in enumerate(nums):
    difference = target - element
    if difference in table:
        print(index, table[difference])
        break
    else:
        table[element] = index


print(table)


