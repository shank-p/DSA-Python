"""
    3. Longest Substring Without Repeating Characters
    - LeetCode
"""

s = input()
maxi = 0
temp  = ''
for i in range(len(s)):
    if s[i] not in temp:
        temp += s[i]
        print('no_prob', temp)
    else:
        if (len(temp) > maxi):
            maxi = len(temp)
        x = temp.index(s[i])
        print('prob', s[i], x)
        temp = temp[x+1:] + s[i] 
        print('new_', temp)
print(max(maxi, len(temp)))
