"""
    Longest Palindromic subsequence
"""

l = []
def subsequence(s, ans, i):
    if (i==len(s)):
        l.append(ans)
        return ans
    subsequence(s, ans + s[i], i+1)
    subsequence(s, ans, i+1)


s = input()
ans = ""
subsequence(s, "", 0)


