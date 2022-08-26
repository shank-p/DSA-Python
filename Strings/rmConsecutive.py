"""
    Remove Consecutive Characters
    - GFG
"""

s = input()
res = [s[0]]

for i in s:
    if (res[-1] != i):
        res.append(i)
print(''.join(res))