"""
    permutations
"""

s = 'abcd'

# 1. for a b c
# 2. _a_ --> possible loc for b
# 3. _b_a_b_ --> possible loc for c
# .. recursive(str[1st_half] + ch + str[2nd_half])
def findPerms(p, up):
    if len(up) == 0:
        print(p)
        return
    char = up[0]
    for i in range(len(p)+1, 2):
        findPerms(p[:i] + char + p[i:], up[1:])

findPerms('', s)

