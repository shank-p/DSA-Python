"""
    reverse a number recursively
"""

import math
n = int(input())

"""
# using outside variable
temp = 0
def rev(n):
    global temp
    if (n%10 == n):
        temp = temp*10 + (n%10)
        return 
    temp = temp*10 + (n%10)
    return rev(n//10)

rev(n)
print(temp)
"""

# using functions only and passing required args
def rev2(n):
    digits = int(math.log10(n)) + 1
    return helper(n, digits)

def helper(n, digits):
    #print (n, digits)
    if (n%10 == n):
        return n
    rem = n % 10
    #print(rem)
    return rem*(10**(digits-1)) + helper(n//10, digits-1)

res = rev2(n)
print(res)
