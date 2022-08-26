"""
    890. Find and Replace Pattern
    - leetCode
"""

words = input().split()
pattern = input()

res = []
for i in words:
    if (len(i) != len(pattern)): 
        continue
    maps = {}
    valid = True
    for k in range(len(i)):
        if (pattern[k] not in maps):
            if (i[k] not in maps.values()):
                maps[pattern[k]] = i[k]
            else:
                valid = False
                break
        else:
            if (maps[pattern[k]] == i[k]):
                continue
            else:
                valid = False
                break
    if (valid):
        res.append(i)
        print('maps' ,maps)
print(res)
