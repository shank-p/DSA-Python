"""
    Pascal's Triangle
"""

rows = int(input())
for i in range(rows):
    icj = 1
    for j in range(i+1):
        print(str(icj), end=" ")
        icjp1 = icj * (i-j)//(j+1)
        icj = icjp1
    print()