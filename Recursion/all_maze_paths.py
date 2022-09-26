"""
    Given a 2D array maze find all possible ways to travel from pnt A to pnt B

    -------------
    | a |   |   |
    -------------
    |   |   |   |
    -------------
    |   |   | b |
    -------------
"""

maze = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

def allPaths(maze, row, col, p):
    if row == len(maze)-1 and col == len(maze[0])-1:
        print(p)
        return
    if maze[row][col] == False:
        return
    maze[row][col] = False
    if row < len(maze) - 1:
        allPaths(maze, row+1, col, p+'D')
    if col < len(maze[0]) - 1:
        allPaths(maze, row, col+1, p+'R')
    if row > 0:
        allPaths(maze, row-1, col, p+'U')
    if col > 0:
        allPaths(maze, row, col-1, p+'L')
    maze[row][col] = True

allPaths(maze, 0, 0, '')
    