"""
    - Binary search on Sorted matrix
"""

matrix = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15], 
    [16, 17, 18, 19, 20], 
    [21, 22, 23, 24, 25]
    ]
target = int(input())

def BinarySearch(arr, target, startCol, endCol, constRow):
    low = startCol
    high = endCol 
    while(low <= high):
        mid = (low + high)//2
        if(arr[constRow][mid] == target):
            print( [constRow, mid])
            break
        elif(arr[constRow][mid] < target):
            low = mid + 1
        else:
            high = mid - 1

startRow = 0
endRow = len(matrix) - 1
midCol = (0 + len(matrix)-1)//2
while (startRow + 1 == endRow ):
    midRow = (startRow + endRow)//2
    if (matrix[midRow][midCol] == target):
        print([midRow, midCol])
        break
    elif (matrix[midRow][midCol] < target):
        startRow = midRow
    else:
        endRow = midRow

if (matrix[startRow][midCol] == target):
    print([startRow][midCol])
elif(matrix[endRow][midCol] == target):
    print([endRow][midCol])

elif (target <= matrix[startRow][midCol-1]):
    BinarySearch(matrix, target, 0, midCol-1, startRow)
elif (target >= matrix[endRow][midCol+1]):
    BinarySearch(matrix, target, midCol+1, len(matrix[0])-1, endRow)
elif (target >=  matrix[startRow][midCol + 1] and target<= matrix[endRow][0]):
    BinarySearch(matrix, target, midCol+1, len(matrix[0]) -1, startRow)
else:
    BinarySearch(matrix, target, 0, midCol-1, endRow)
