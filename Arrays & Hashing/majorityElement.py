"""
    169. Majority Element
    -leetCode
"""

nums = list(map(int, input().split()))

n = len(nums)
dictionary = {}

for i in nums:
    if i not in dictionary:
        dictionary[i] = 0
    dictionary[i] += 1

    if (dictionary[i] > n//2):
        print(i)
        break
