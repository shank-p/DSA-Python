"""
    All combinations of dice to sum upto a target number
"""

target = 4

def diceRolls(p, up):
    if up == 0:
        print(p)
        return
    for i in range(1,up+1):
        diceRolls(p+str(i), up-i)

diceRolls('', target)