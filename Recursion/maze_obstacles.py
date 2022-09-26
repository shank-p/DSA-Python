"""
    Maze with obstacles.
    -> bool arr.
    -> go right or down
"""

maze = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]

def mazeObstacles(maze: list[list[bool]], p, row, col):
    if row == len(maze)-1 and col == len(maze[0])-1:
        print(p)
        return
    if (not maze[row][col]):
        return
    if row < len(maze)-1:
        mazeObstacles(maze, p + 'D', row + 1, col)
    if col < len(maze[0])-1:
        mazeObstacles(maze, p + 'R', row, col+1)

mazeObstacles(maze, '', 0, 1)
    
