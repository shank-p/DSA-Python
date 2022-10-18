"""
    n_knights
"""

n = 4
board = []
for _ in range(n):
    board.append([False]*n)

def nKnights(board, row, col, Kcount):
    if Kcount == 0:
        printBoard(board)
        return 1
    count = 0
    if col == len(board):
        count += nKnights(board, row + 1, 0, Kcount)
        return count
    if row == len(board)-1 and col >= len(board)-1:
        return 0
    if isSafe(board, row, col):
        board[row][col] = True
        count += nKnights(board, row, col + 1, Kcount - 1)
        board[row][col] = False
    count += nKnights(board, row, col + 1, Kcount)
    return count

def printBoard(board):
    pass

def isSafe(board, row, col):
    if isValid(board, row-2, col-1):
        if board[row-2][col-1] == True:
            return False
    if isValid(board, row-2, col+1):
        if board[row-2][col+1] == True:
            return False
    if isValid(board, row-1, col-2):
        if board[row-1][col-2] == True:
            return False
    if isValid(board, row-1, col+2):
        if board[row-1][col+2] == True:
            return False
    
    return True

def isValid(board, row, col):
    if (row >=0 and row < len(board)) and (col >=0 and col <len(board)):
        return True
    return False

print(nKnights(board, 0, 0, n))
            