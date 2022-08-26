"""
    54. Spiral Matrix
    - leetcode
"""

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
trace = []
rows = len(matrix) 
cols = len(matrix[0])

st_row = 0
en_row = rows 
st_col = 0
en_col = cols 

while (st_row < en_row) :
    for i in range(st_col, en_col):
        print('1st')
        trace.append(matrix[st_row][i])
    st_row += 1
    for i in range(st_row, en_row):
        print('2nd')
        trace.append(matrix[i][en_col - 1])
    en_col -= 1
    if (len(trace) == rows*cols):
        break
    for i in range(en_col-1 , st_col -1, -1):
        print('3rd')
        trace.append(matrix[en_row-1][i])
    en_row -= 1
    for i in range(en_row-1, st_row-1, -1):
        print('4th')
        trace.append(matrix[i][st_col])
    st_col += 1
    print()
print(trace)