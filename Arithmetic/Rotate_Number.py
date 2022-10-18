"""
    To rotate a number at a given pivot position
"""

import math


n = int(input())
p = int(input())

def rotate(n: int, p: int) -> int:
    numLen = int(math.log10(n)) + 1
    p = p % numLen
    br = numLen - p
    half2 = n % (10**br)
    half1 = n // (10**br)
    return (half2*(10**p) + half1)

res = rotate(n, p)
print(res)


