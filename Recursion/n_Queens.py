"""
    nQueens
"""

n = 5
board = []
for _ in range(n):
    board.append([False]*n)


def nQueens(board, row):
    if row == len(board):
        printBoard(board)
        #print()
        return 1
    count = 0
    for col in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = True
            count += nQueens(board, row + 1)
            board[row][col] = False
    return count

def isSafe(board, row, col):
    for i in range(row):
        if board[i][col] == True:
            return False

    maxLeft = min(row, col)
    for i in range(1, maxLeft+1):
        if board[row-i][col-i] == True:
            return False
    
    maxRight = min(row, len(board)-col -1)
    for i in range(1, maxRight + 1):
        if board[row-i][col+i] == True:
            return False
    return True
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]:
                print('Q ', end='')
            else:
                print('X ', end='')
        print()
    print('\n')

print(nQueens(board, 0))