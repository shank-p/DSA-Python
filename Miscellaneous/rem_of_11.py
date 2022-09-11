"""
    Find the remainder of n by 11
"""

n = input()
sum = 0
for i in range(len(n)):
    if i & 1:
        sum -= int(n[i])
    else:
        sum += int(n[i])
print(sum %11)