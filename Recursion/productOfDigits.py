"""
    Product of digits of a number recursively
"""

n = int(input())

def product(n):
    if (n%10 ==n ):
        return n
    rem = n % 10
    return rem * product(n//10)

result = product(n)
print(result)