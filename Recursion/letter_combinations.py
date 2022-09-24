"""
    Letter Combinations of a phone number.
"""

digits = "23" # op -> ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

d = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

op = []
def lettetCombinations(p, up):
    if len(up) == 1:
        for j in d[int(up)]:
            print(p + j)
        return
    for i in range(len(up)):
        lettetCombinations(p + up[i], up[i:])
lettetCombinations('', digits)

