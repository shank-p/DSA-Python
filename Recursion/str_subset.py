"""
    subsequence in strings
"""

s = 'abcded'
strings = []

def subsequence(s, i, sub_s):
    if len(s) == i:
        if sub_s not in strings:
            strings.append(sub_s)
        return
    subsequence(s, i+1, sub_s + s[i])
    subsequence(s, i+1, sub_s)
   

subsequence(s, 0, '')
print(strings)


