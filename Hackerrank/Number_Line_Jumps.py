"""
    Number Line Jumps
    - Hackerrank
"""

def kangaroo(x1, v1, x2, v2):
    if (x1<x2 and v1<v2) or (x1>x2 and v1>v2):
        return 'NO'
    try:
        num = (x2-x1)/(v2-v1)
        # use is_integer() instead of isinstance() 
        if num.is_integer():
            return 'YES'
    except: return 'NO'
    return 'NO'
    
# single line input
inputs = list(map(int, input().split()))
x1 = inputs[0]
v1 = inputs[1]
x2 = inputs[2]
v2 = inputs[3]

result = kangaroo(x1, v1, x2, v2)
print(result)