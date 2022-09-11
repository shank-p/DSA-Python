"""
    Longest pallindromic substrings
"""

s = input()

subs = []
ans = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        temp = s[i:j]
        if len(temp) <= ans:
            continue
        if temp == temp[::-1]:
            ans = len(temp)

print(ans)