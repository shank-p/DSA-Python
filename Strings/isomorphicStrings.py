"""
    205. Isomorphic Strings
    - LeetCode
"""

s = input()
t = input()

maps = {}

if (len(s)!=len(t)):
    exit()

for i in range(len(s)):
    if (s[i] not in maps):
        if (t[i] not in maps.values()):
            maps[s[i]] = t[i]
        else:
            print(-1)
            break
    else:
        if (t[i] == maps[s[i]]):
            continue
        else:
            print(-1)
            break
    print(maps)
