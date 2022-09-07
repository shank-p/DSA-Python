"""
    recursive sum of digits of a number
"""

num = int(input())

def sum(num):
    if (num == 0):
        return 0
    rem = num % 10
    return rem + sum(num//10)

result = sum(num)
print(result)