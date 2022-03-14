# https://leetcode.com/problems/search-a-2d-matrix/

# Write an efficient algorithm that searches for a value target in an m x n 
# integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.


def findNum(matrix, target):
    def binSearchRow(matrix, target, start, end):
        middle = (start + end) // 2

        if start > end:
            return -1
        if matrix[middle][0] <= target <= matrix[middle][-1]:
            return middle
        elif target > matrix[middle][-1]:
            return binSearchRow(matrix, target, middle + 1, end)
        else:
            return binSearchRow(matrix, target, start, middle - 1)
    
    def binSearchNum(row, target, start, end):
        middle = (start + end) // 2

        if start > end:
            return False

        if row[middle] == target: return True

        if target > row[middle]:
            return binSearchNum(row, target, middle + 1, end)
        else:
            return binSearchNum(row, target, start, middle - 1)

    target_row = binSearchRow(matrix, target, 0, len(matrix) - 1)

    if target_row == -1: return False

    return binSearchNum(matrix[target_row], target, 0, len(matrix[target_row]))


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 70

    print(findNum(matrix, target))