"""
    - Search in row-wise and col-wise sorted matrix
    
    [ [10, 20, 30, 40], 
      [15, 25, 35, 45], 
      [28, 29, 37, 49],
      [33, 34, 38, 50] ]

"""

matrix = [  [10, 20, 30, 40], 
            [15, 25, 35, 45], 
            [28, 29, 37, 49],
            [33, 34, 38, 50]  ]
target = int(input())

row = 0
col = len(matrix) - 1

while (row <= len(matrix) - 1 and col >= 0):
    if (matrix[row][col] == target):
        print([row, col])
        break
    elif (matrix[row][col] < target):
        row += 1
    else:
        col -= 1

