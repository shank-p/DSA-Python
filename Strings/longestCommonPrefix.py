"""
    14. Longest Common Prefix
    - LeetCode
"""

strs = list(input().split())

prefix = ""
Exit = False
for i in range(len(strs[0])):
    prefix += strs[0][i]
    for j in strs:
        if j[:i + 1] != prefix:
            print(prefix[:-1])
            Exit = True
            break
    if (Exit): break