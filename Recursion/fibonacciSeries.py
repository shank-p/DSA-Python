"""
    Fibonacci value of a number.
"""

num = int(input())
def fib(n):
    if (n<2):
        return n
    return(fib(n-1) + fib(n-2))

ans = fib(num)
print(ans)
