"""
    1295. Find Numbers with Even Number of Digits
    - leetcode
"""
import math

nums = list(map(int, input().split()))
count = 0

"""
for i in nums :
    if len(str(i))%2 == 0:
        count+= 1
print(count)
"""

for i in nums:
    digits = int(math.log10(i)) + 1
    if digits %2 == 0:
        count += 1

# can be used to count the number of digits in binary, octal  as == {log2(i), log8(i)}