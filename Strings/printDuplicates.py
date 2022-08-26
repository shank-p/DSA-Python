"""
    Print all the duplicates in the input string
    - GFG
"""

s = input()

maps = {}
for i in s:
    maps[i]  = maps.get(i, 0) + 1

for key, val in maps.items():
    if (val > 1):
        print(key, val)