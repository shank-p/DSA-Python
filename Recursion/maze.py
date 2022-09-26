"""
    Given a maze grid(ex: 3x3) find the no of ways from A to B

    -------------
    | a |   |   |
    -------------
    |   |   |   |
    -------------
    |   |   | b |
    -------------

    only can move right or down
"""

# maze size
l, b = map(int, input().split())

def paths(row, col):
    if row == 1 or col == 1:
        # also can be, row = length-1 or col = length-1
        return 1
    right = paths(row, col-1)
    down = paths(row-1, col)
    return right + down

print(paths(b, l))

def printpaths(row, col, p):
    if row == 1 and col == 1:
        print(p)
        return
    if col > 1:
        right = printpaths(row, col-1, p+'R')
    if row > 1:
        left = printpaths(row-1, col, p+'D')
    if row > 1 and col > 1:
        diagonal = printpaths(row-1, col-1, p+'V')



printpaths(b, l, '')