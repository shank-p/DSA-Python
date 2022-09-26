"""
    Letter Combinations of a phone number.
"""

digits = "4598" # op -> ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

d = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

op = []
def lettetCombinations(p, up):
    if len(up) == 0:
        #print(p)
        op.append(p)
        return
    digit = int(up[0])
    al = d[digit]
    for i in range(len(al)):
        char = al[i]
        lettetCombinations(p + char, up[1:])

lettetCombinations('', digits)
print(op)
