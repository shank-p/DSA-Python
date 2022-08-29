"""
    1431. Kids With the Greatest Number of Candies
    - leetCode
"""

candies = list(map(int, input().split()))
extraCandies = int(input())

result = []
curMax = max(candies)
for i in candies:
    if (i + extraCandies >= curMax):
        result.append(True)
    else:
        result.append(False)
print(result)