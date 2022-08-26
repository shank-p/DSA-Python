"""
    20. Valid Parentheses
    - LeetCode
"""

s = input()
stack = []
brackets = {'(':')', '[':']', '{':'}'}

for i in s:
    if brackets.get(i, False):
        stack.append(i)
        print(stack)
        continue
    try:
        if brackets[stack[-1]] != i:
            print(-1)
            break
        stack.pop()
    except : 
        print(-1)
        break 
if (len(stack) != 0):
    print(-1)